from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from accounts.models import SubjectScore


class SubjectScoreSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.full_name')
    class_name = serializers.CharField(source='class_name.class_name')
    subject_name = serializers.CharField(source='subject.name')

    class Meta:
        model = SubjectScore
        fields = ['student_name', 'class_name', 'subject_name', 'semester', 'midterm_score', 'final_score',
                  'final_exam_score']


class SubjectScoreList(APIView):
    def get(self, request, *args, **kwargs):
        class_id = request.query_params.get('class_id')
        subject_id = request.query_params.get('subject_id')
        semester = request.query_params.get('semester')

        scores = SubjectScore.objects.filter(
            class_name__id=class_id,
            subject__id=subject_id,
            semester=semester
        )

        serializer = SubjectScoreSerializer(scores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
