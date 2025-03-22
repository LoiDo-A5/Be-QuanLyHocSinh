from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from accounts.models import User, StudentScore
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import action

class UserPagination(PageNumberPagination):
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

class StudentScoreSerializer(serializers.ModelSerializer):
    semester_1_avg = serializers.FloatField()
    semester_2_avg = serializers.FloatField()

    class Meta:
        model = StudentScore
        fields = ['semester_1_avg', 'semester_2_avg']

class UserListSerializer(serializers.ModelSerializer):
    student_score = serializers.SerializerMethodField()
    class_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'full_name', 'gender', 'birthday', 'address', 'email', 'phone_number',
                  'is_phone_verified', 'avatar', 'time_zone', 'role', 'student_score', 'class_name')

    def get_student_score(self, obj):
        student_score = StudentScore.objects.filter(student=obj).first()
        if student_score:
            return {
                "semester_1_avg": student_score.semester_1_avg,
                "semester_2_avg": student_score.semester_2_avg,
            }
        return None

    def get_class_name(self, obj):
        student_score = StudentScore.objects.filter(student=obj).first()
        if student_score and student_score.class_name:
            class_name = f"{student_score.class_name.level.level_name}{student_score.class_name.class_name}"
            return class_name
        return 'Không có lớp'

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserListSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = UserPagination

    @action(detail=False, methods=['get'])
    def list_student(self, request):
        students = User.objects.filter(role=1)

        page = self.paginate_queryset(students)
        if page is not None:
            serializer = UserListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = UserListSerializer(students, many=True)
        return Response(serializer.data)