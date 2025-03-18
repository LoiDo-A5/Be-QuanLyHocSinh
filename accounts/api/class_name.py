from rest_framework import viewsets
from rest_framework import serializers
from accounts.models.class_name import ClassName

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
