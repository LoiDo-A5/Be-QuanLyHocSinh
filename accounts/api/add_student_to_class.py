from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from rest_framework import serializers

from accounts.models import User, ClassName, ClassStudent


class ClassStudentSerializer(serializers.ModelSerializer):
    student_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='student')
    class_id = serializers.PrimaryKeyRelatedField(queryset=ClassName.objects.all(), source='class_name')

    class Meta:
        model = ClassStudent
        fields = ['student_id', 'class_id']

class AddStudentToClass(APIView):

    def post(self, request):
        student_id = request.data.get('student_id')
        class_id = request.data.get('class_id')

        if not student_id or not class_id:
            return Response({'error': 'Both student_id and class_id are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            class_student = ClassStudent.objects.create(student_id=student_id, class_name_id=class_id)
            return Response({'success': True, 'data': ClassStudentSerializer(class_student).data},
                            status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
