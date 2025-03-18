from django.db import models
from accounts.models.class_level import ClassLevel
from django.core.exceptions import ValidationError

MAX_STUDENTS = 40


class ClassName(models.Model):
    level = models.ForeignKey(ClassLevel, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=10)
    number_of_students = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.level.level_name} - {self.class_name}"

    def clean(self):
        if self.number_of_students > MAX_STUDENTS:
            raise ValidationError(f"Số học sinh không được vượt quá {MAX_STUDENTS} học sinh.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
