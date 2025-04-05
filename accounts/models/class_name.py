from django.db import models
from django.core.exceptions import ValidationError

from accounts.models.class_level import ClassLevel


class ClassName(models.Model):
    level = models.ForeignKey(ClassLevel, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=10)
    number_of_students = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.level.level_name} - {self.class_name}"

    def clean(self):
        from accounts.models import SystemSetting
        try:
            system_setting = SystemSetting.objects.first()
            if system_setting and self.number_of_students > system_setting.max_students_per_class:
                raise ValidationError(
                    f"Số học sinh không được vượt quá {system_setting.max_students_per_class} học sinh.")
        except SystemSetting.DoesNotExist:
            raise ValidationError("Chưa cấu hình SystemSetting.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
