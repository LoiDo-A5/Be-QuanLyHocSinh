from datetime import date

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


class USER_ROLE:
    STUDENT = 1
    TEACHER = 2
    ADMIN = 3


USER_ROLE_CHOICES = (
    (USER_ROLE.STUDENT, 'Học sinh'),
    (USER_ROLE.TEACHER, 'Giáo viên'),
    (USER_ROLE.ADMIN, 'Quản trị viên'),
)


class User(AbstractUser):
    full_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.IntegerField(
        choices=[(0, 'Male'), (1, 'Female')],
        default=0,
    )
    birthday = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    is_phone_verified = models.BooleanField(default=False)
    avatar = models.ImageField(null=True, blank=True)

    phone_number = models.CharField(max_length=50, null=True, blank=True)
    time_zone = models.CharField(max_length=50, default='Asia/Ho_Chi_Minh', blank=True)

    role = models.IntegerField(
        choices=USER_ROLE_CHOICES,
        blank=True,
        null=True,
        default=USER_ROLE.STUDENT,
    )

    @property
    def age(self):
        today = date.today()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))

    def clean(self):
        if self.role == USER_ROLE.STUDENT:
            if self.age < 15 or self.age > 20:
                raise ValidationError("Học sinh phải có độ tuổi từ 15 đến 20.")
