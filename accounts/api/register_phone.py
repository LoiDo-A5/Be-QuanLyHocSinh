from django.utils.translation import gettext
from rest_framework import serializers
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from accounts.models import User

class RegisterPhoneSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(max_length=100, required=True)
    gender = serializers.ChoiceField(choices=[(0, 'Male'), (1, 'Female')], required=True)
    birthday = serializers.DateField(required=True)
    address = serializers.CharField(max_length=255, required=True)

    class Meta:
        model = User
        fields = (
            'full_name',
            'email',
            'gender',
            'birthday',
            'address',
            'time_zone',
        )

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(gettext('This email is already in use'))
        return email

    def validate(self, attrs):
        attrs = super().validate(attrs)
        return attrs

    def validate_time_zone(self, time_zone):
        if not time_zone:
            time_zone = 'Asia/Ho_Chi_Minh'
        return time_zone

    def create(self, validated_data):
        return super().create(validated_data)


class RegisterPhoneApi(GenericAPIView):
    serializer_class = RegisterPhoneSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email_exists = User.objects.filter(email=serializer.validated_data['email']).exists()

        if email_exists:
            error_message = gettext('Email already exists')
            return Response({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)

        User.objects.create(
            username=serializer.validated_data['email'],
            email=serializer.validated_data['email'],
            full_name=serializer.validated_data['full_name'],
            gender=serializer.validated_data['gender'],
            birthday=serializer.validated_data['birthday'],
            address=serializer.validated_data['address'],
            time_zone=serializer.validated_data.get('time_zone', 'Asia/Ho_Chi_Minh'),
        )

        return Response(
            {
                'message': gettext('Create user success'),
            }, status.HTTP_200_OK,
        )
