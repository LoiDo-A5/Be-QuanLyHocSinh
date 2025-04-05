from rest_framework import viewsets
from rest_framework import serializers
from accounts.models.class_name import ClassName
from rest_framework.response import Response
from rest_framework import status


class ClassNameSerializer(serializers.ModelSerializer):
    level_name = serializers.CharField(source='level.level_name', read_only=True)

    class Meta:
        model = ClassName
        fields = ['id', 'level', 'class_name', 'number_of_students', 'level_name']

    def update(self, instance, validated_data):
        instance.class_name = validated_data.get('class_name', instance.class_name)
        instance.number_of_students = validated_data.get('number_of_students', instance.number_of_students)

        level_data = validated_data.get('level', None)
        if level_data:
            instance.level = level_data

        instance.save()
        return instance


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

