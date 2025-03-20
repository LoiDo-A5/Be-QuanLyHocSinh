from django.db import models
from accounts.models import User
from accounts.models import ClassName
from accounts.models.subject import Subject

class SubjectScore(models.Model):
    SEMESTER_CHOICES = [
        (1, 'Học kỳ 1'),
        (2, 'Học kỳ 2'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    class_name = models.ForeignKey(ClassName, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    semester = models.IntegerField(choices=SEMESTER_CHOICES)  # Học kỳ (1 hoặc 2)
    midterm_score = models.FloatField(null=True, blank=True)  # Điểm 15 phút hoặc giữa kỳ
    final_score = models.FloatField(null=True, blank=True)  # Điểm 1 tiết hoặc cuối kỳ
    final_exam_score = models.FloatField(null=True, blank=True)  # Điểm cuối học kỳ

    def __str__(self):
        return f"{self.student.full_name} - {self.subject.name} - {self.class_name}"

    class Meta:
        unique_together = ['student', 'subject', 'class_name', 'semester']
