from rest_framework import viewsets
from rest_framework import serializers
from accounts.models.class_level import ClassLevel
from rest_framework.response import Response
from rest_framework.decorators import action

class ClassLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassLevel
        fields = ['id', 'level_name']

class ClassLevelViewSet(viewsets.ModelViewSet):
    queryset = ClassLevel.objects.all()
    serializer_class = ClassLevelSerializer
