from django.db import models

from accounts.models import User
from django.core.exceptions import ValidationError


class ClassStudent(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    class_name = models.ForeignKey('accounts.ClassName', on_delete=models.CASCADE)
