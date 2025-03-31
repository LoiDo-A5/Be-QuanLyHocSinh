from rest_framework import viewsets
from rest_framework import serializers

from accounts.models import SystemSetting
from accounts.models.user import USER_ROLE
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class SystemSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSetting
        fields = ['min_student_age', 'max_student_age']


class SystemSettingViewSet(viewsets.ModelViewSet):
    queryset = SystemSetting.objects.all()
    serializer_class = SystemSettingSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'create']:
            if self.request.user.role == USER_ROLE.STUDENT:
                self.permission_denied(self.request, message="Only admins can modify system settings.")
        return super().get_permissions()
