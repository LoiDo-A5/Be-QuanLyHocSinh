from rest_framework import viewsets
from rest_framework import serializers
from accounts.models.class_name import ClassName
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
        try:
            return super().create(request, *args, **kwargs)
        except PermissionError as e:
            return Response({'error': str(e)}, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except PermissionError as e:
            return Response({'error': str(e)}, status=status.HTTP_403_FORBIDDEN)
