from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)  # Tên môn học
    code = models.CharField(max_length=20)  # Mã môn học (nếu có)

    def __str__(self):
        return self.name
