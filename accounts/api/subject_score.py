from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers

from accounts.models import SubjectScore


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

        if created:
            return Response({'message': 'Điểm đã được tạo mới', 'data':
                SubjectScoreSerializer(subject_score).data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Điểm đã được cập nhật', 'data':
                SubjectScoreSerializer(subject_score).data}, status=status.HTTP_200_OK)
