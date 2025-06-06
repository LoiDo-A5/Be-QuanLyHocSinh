from django.db.models import Count, Q, F, ExpressionWrapper, FloatField
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import SubjectScore, ClassName, Subject, SystemSetting


class SubjectReportView(APIView):

    def get(self, request):
        subject_id = request.query_params.get("subject_id")
        semester = request.query_params.get("semester")

        if not subject_id or not semester:
            return Response({"error": "Vui lòng cung cấp subject_id và semester"}, status=400)

        try:
            subject = Subject.objects.get(id=subject_id)
        except Subject.DoesNotExist:
            return Response({"error": "Môn học không tồn tại"}, status=404)

        system_setting, _ = SystemSetting.objects.get_or_create()
        pass_score = system_setting.pass_score
        # Tính điểm trung bình môn theo công thức: (giữa kỳ * 1 + cuối kỳ * 2 + thi cuối kỳ * 3) / 6
        class_reports = (
            SubjectScore.objects
            .filter(subject=subject, semester=semester)
            .annotate(
                avg_score=ExpressionWrapper(
                    (F('midterm_score') * 1 + F('final_score') * 2 + F('final_exam_score') * 3) / 6.0,
                    output_field=FloatField()
                )
            )
            .values('class_name')
            .annotate(
                total_students=Count('student', distinct=True),
                passed_students=Count('student', filter=Q(avg_score__gte=pass_score), distinct=True)  # Điều kiện đạt môn
            )
        )

        report_data = []
        for index, class_data in enumerate(class_reports, start=1):
            class_obj = ClassName.objects.select_related('level').get(id=class_data['class_name'])
            class_name = f"{class_obj.level.level_name}{class_obj.class_name}"
            total_students = class_data['total_students']
            passed_students = class_data['passed_students']
            pass_rate = round((passed_students / total_students) * 100, 2) if total_students > 0 else 0

            report_data.append({
                "stt": index,
                "class_name": class_name,
                "total_students": total_students,
                "passed_students": passed_students,
                "pass_rate": f"{pass_rate}%"
            })

        return Response({
            "subject": subject.name,
            "semester": semester,
            "report": report_data
        })
