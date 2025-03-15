from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from accounts.models import User
from rest_framework import serializers


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'full_name', 'gender', 'birthday', 'address', 'email', 'phone_number',
                  'is_phone_verified', 'avatar', 'time_zone', 'role')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = (IsAuthenticated,)
