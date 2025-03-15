from django.db import models

from accounts.models.class_level import ClassLevel

MAX_STUDENTS = 40

class ClassName(models.Model):
    level = models.ForeignKey(ClassLevel, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=10)
    number_of_students = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.level.level_name} - {self.class_name}"

