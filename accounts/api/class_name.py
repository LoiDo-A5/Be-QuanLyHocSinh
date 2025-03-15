from rest_framework import viewsets
from rest_framework import serializers
from accounts.models.class_name import ClassName

class ClassNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassName
        fields = ['id', 'level', 'class_name', 'number_of_students']

class ClassNameViewSet(viewsets.ModelViewSet):
    queryset = ClassName.objects.all()
    serializer_class = ClassNameSerializer
