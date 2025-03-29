from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import ClassName, StudentScore
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
            student_scores = StudentScore.objects.filter(class_name=class_obj)
            total_students = student_scores.count()

            if total_students == 0:
                passed_students = 0
            else:
                if semester == 1:
                    passed_students = student_scores.filter(semester_1_avg__gte=5).count()
                else:
                    passed_students = student_scores.filter(semester_2_avg__gte=5).count()

            passed_ratio = round((passed_students / total_students) * 100, 2) if total_students > 0 else 0

            report_data.append({
                "class_name": str(class_obj),
                "total_students": total_students,
                "passed_students": passed_students,
                "passed_ratio": passed_ratio
            })

        serializer = SemesterReportSerializer(report_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
