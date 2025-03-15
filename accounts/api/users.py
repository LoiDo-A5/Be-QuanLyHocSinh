from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from accounts.models import User
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class ArtworkPagination(PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        data_response = {
            'page_size': self.page_size,
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        }
        return Response(data_response)

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'full_name', 'gender', 'birthday', 'address', 'email', 'phone_number',
                  'is_phone_verified', 'avatar', 'time_zone', 'role')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserListSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = ArtworkPagination
