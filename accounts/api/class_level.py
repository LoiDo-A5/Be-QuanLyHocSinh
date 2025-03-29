from rest_framework import viewsets
from rest_framework import serializers
from accounts.models.class_level import ClassLevel
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from accounts.models.user import USER_ROLE


class ClassLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassLevel
        fields = ['id', 'level_name']

class ClassLevelViewSet(viewsets.ModelViewSet):
    queryset = ClassLevel.objects.all()
    serializer_class = ClassLevelSerializer

    def create(self, request, *args, **kwargs):
        if request.user.role == USER_ROLE.STUDENT:
            return Response({'error': 'Students are not allowed to create class levels.'},
                            status=status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if request.user.role == USER_ROLE.STUDENT:
            return Response({'error': 'Students are not allowed to update class levels.'},
                            status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)