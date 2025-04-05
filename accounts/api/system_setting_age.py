from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from accounts.models import SystemSetting


class SystemSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSetting
        fields = ['min_student_age', 'max_student_age']


class SystemSettingView(APIView):
    def get(self, request):
        setting, _ = SystemSetting.objects.get_or_create()
        serializer = SystemSettingSerializer(setting)
        return Response(serializer.data)

    def put(self, request):
        setting, _ = SystemSetting.objects.get_or_create()
        serializer = SystemSettingSerializer(setting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
