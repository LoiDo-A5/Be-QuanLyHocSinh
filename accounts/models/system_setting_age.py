from django.db import models
from django.core.exceptions import ValidationError

class SystemSetting(models.Model):
    min_student_age = models.PositiveIntegerField(default=15)
    max_student_age = models.PositiveIntegerField(default=20)

    def save(self, *args, **kwargs):
        if self.min_student_age >= self.max_student_age:
            raise ValidationError("Tuổi tối thiểu phải nhỏ hơn tuổi tối đa.")
        super().save(*args, **kwargs)

    def __str__(self):
        return "System Settings"
