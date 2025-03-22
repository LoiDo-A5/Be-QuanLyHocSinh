from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from accounts.models import SubjectScore, StudentScore, ClassStudent

class SubjectScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectScore
        fields = ['id', 'student', 'class_name', 'subject', 'semester', 'midterm_score',
                  'final_score', 'final_exam_score']

class SubjectScoreCreateUpdateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        student_id = request.data.get('student')
        class_id = request.data.get('class_name')
        subject_id = request.data.get('subject')
        semester = request.data.get('semester')

        if not all([student_id, class_id, subject_id, semester]):
            return Response({
                'message': 'Missing required fields: student, class_name, subject, or semester'
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            subject_score, created = SubjectScore.objects.update_or_create(
                student_id=student_id,
                class_name_id=class_id,
                subject_id=subject_id,
                semester=semester,
                defaults={
                    'midterm_score': request.data.get('midterm_score'),
                    'final_score': request.data.get('final_score'),
                    'final_exam_score': request.data.get('final_exam_score'),
                }
            )

            class_student = ClassStudent.objects.filter(
                student_id=student_id,
                class_name_id=class_id
            ).first()

            if not class_student:
                return Response({
                    'message': 'Student is not enrolled in this class'
                }, status=status.HTTP_400_BAD_REQUEST)

            student_score_instance, created = StudentScore.objects.update_or_create(
                student_id=student_id,
                class_name_id=class_id,
                defaults={
                    'is_calculated': False,
                }
            )

            student_score_instance.calculate_semester_1_avg()
            student_score_instance.calculate_semester_2_avg()
            student_score_instance.save()

            return Response({
                'message': 'Score created or updated successfully',
                'data': SubjectScoreSerializer(subject_score).data
            }, status=status.HTTP_200_OK if created else status.HTTP_201_CREATED)

        except Exception as e:
            return Response({
                'message': f'An error occurred: {str(e)}'
            }, status=status.HTTP_400_BAD_REQUEST)
