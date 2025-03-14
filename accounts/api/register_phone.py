from django.utils.translation import gettext
from rest_framework import serializers
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from accounts.models import User
from django.contrib.auth.hashers import make_password


class RegisterPhoneSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    full_name = serializers.CharField(max_length=100, required=True)
    gender = serializers.ChoiceField(choices=[(0, 'Male'), (1, 'Female')], required=True)
    birthday = serializers.DateField(required=True)
    address = serializers.CharField(max_length=255, required=True)

    class Meta:
        model = User
        fields = (
            'full_name',
            'email',
            'password1',
            'password2',
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
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError(gettext("The two password fields didn't match."))

        attrs['password'] = make_password(attrs['password1'])

        return attrs

    def validate_time_zone(self, time_zone):
        if not time_zone:
            time_zone = 'Asia/Ho_Chi_Minh'
        return time_zone

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
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
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password'],
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
