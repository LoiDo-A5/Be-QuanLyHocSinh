from rest_framework import viewsets
from rest_framework import serializers
from accounts.models.class_name import ClassName
from accounts.models.user import USER_ROLE
from rest_framework.response import Response
from rest_framework import status

class ClassNameSerializer(serializers.ModelSerializer):
    level_name = serializers.SerializerMethodField()

    class Meta:
        model = ClassName
        fields = ['id', 'level', 'class_name', 'number_of_students', 'level_name']

    def get_level_name(self, obj):
        return obj.level.level_name if obj.level else None

class ClassNameViewSet(viewsets.ModelViewSet):
    queryset = ClassName.objects.all()
    serializer_class = ClassNameSerializer

    def create(self, request, *args, **kwargs):
        if request.user.role == USER_ROLE.STUDENT:
            return Response({'error': 'Students are not allowed to create class names.'},
                            status=status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if request.user.role == USER_ROLE.STUDENT:
            return Response({'error': 'Students are not allowed to update class names.'},
                            status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)