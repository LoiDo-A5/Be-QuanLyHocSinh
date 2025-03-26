from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from accounts.models import ClassName, ClassStudent
from accounts.models import User

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name', 'gender', 'birthday', 'address']

class ClassInfoSerializer(serializers.ModelSerializer):
    students = StudentSerializer(source='classstudent_set', many=True)

    class Meta:
        model = ClassName
        fields = ['class_name', 'number_of_students', 'students']

class Pagination(PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        data_response = {
            'page_size': self.page_size,
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        }
        return Response(data_response)

class ClassListAPIView(APIView):
    pagination_class = Pagination

    def get(self, request):
        class_id = request.query_params.get('class_id')

        classes = ClassName.objects.filter(id=class_id)

        if not classes:
            return Response({'error': 'Không tìm thấy lớp học nào'}, status=status.HTTP_404_NOT_FOUND)

        class_obj = classes.first()

        class_data = {
            'class_name': class_obj.class_name,
            'number_of_students': class_obj.number_of_students,
            'students': []
        }

        class_students = ClassStudent.objects.filter(class_name=class_obj)

        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(class_students, request)

        for class_student in result_page:
            student_info = {
                'full_name': class_student.student.full_name,
                'gender': class_student.student.gender,
                'birthday': class_student.student.birthday,
                'address': class_student.student.address,
            }
            class_data['students'].append(student_info)

        return paginator.get_paginated_response(class_data)
