from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import ClassName, SubjectScore, ClassStudent
from rest_framework import serializers

class SemesterReportSerializer(serializers.Serializer):
    class_name = serializers.CharField()
    total_students = serializers.IntegerField()
    passed_students = serializers.IntegerField()
    passed_ratio = serializers.FloatField()

class SemesterReportAPIView(APIView):
    def get(self, request):
        semester = request.query_params.get('semester')
        if semester not in ['1', '2']:
            return Response({'error': 'Semester must be 1 or 2'}, status=status.HTTP_400_BAD_REQUEST)

        semester = int(semester)
        report_data = []

        classes = ClassName.objects.all()

        for class_obj in classes:
            # Lấy danh sách học sinh của lớp
            student_ids = ClassStudent.objects.filter(class_name=class_obj).values_list('student_id', flat=True)
            total_students = student_ids.count()
            passed_students = 0

            for student_id in student_ids:
                # Lấy điểm tất cả các môn của học sinh trong học kỳ
                subject_scores = SubjectScore.objects.filter(
                    student_id=student_id,
                    class_name=class_obj,
                    semester=semester
                )

                # Nếu thiếu điểm thì coi là chưa đủ điều kiện
                if not subject_scores.exists():
                    continue

                is_passed = True
                for score in subject_scores:
                    total = 0
                    weight = 0

                    if score.midterm_score is not None:
                        total += score.midterm_score * 1
                        weight += 1
                    if score.final_score is not None:
                        total += score.final_score * 2
                        weight += 2
                    if score.final_exam_score is not None:
                        total += score.final_exam_score * 3
                        weight += 3

                    if weight == 0 or (total / weight) < 5:
                        is_passed = False
                        break

                if is_passed:
                    passed_students += 1

            passed_ratio = round((passed_students / total_students) * 100, 2) if total_students > 0 else 0

            report_data.append({
                "class_name": str(class_obj),
                "total_students": total_students,
                "passed_students": passed_students,
                "passed_ratio": passed_ratio
            })

        serializer = SemesterReportSerializer(report_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
