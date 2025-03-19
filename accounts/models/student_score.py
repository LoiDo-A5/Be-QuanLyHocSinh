from django.db import models
from accounts.models import User
from accounts.models import ClassName

class StudentScore(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    class_name = models.ForeignKey(ClassName, on_delete=models.CASCADE)
    semester_1_avg = models.FloatField(null=True, blank=True)  # Điểm trung bình học kỳ 1
    semester_2_avg = models.FloatField(null=True, blank=True)  # Điểm trung bình học kỳ 2

    def __str__(self):
        return f"{self.student.full_name} - {self.class_name}"

    class Meta:
        unique_together = ['student', 'class_name']
