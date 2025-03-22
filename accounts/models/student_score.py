from django.db import models
from accounts.models import User, ClassName
from accounts.models.subject_score import SubjectScore

class StudentScore(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    class_name = models.ForeignKey(ClassName, on_delete=models.CASCADE)
    semester_1_avg = models.FloatField(null=True, blank=True)
    semester_2_avg = models.FloatField(null=True, blank=True)
    is_calculated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.full_name} - {self.class_name}"

    def _calculate_avg(self, semester):
        subject_scores = SubjectScore.objects.filter(
            student=self.student,
            class_name=self.class_name,
            semester=semester
        )

        if not subject_scores.exists():
            return None

        total_score = 0
        total_weight = 0

        for subject_score in subject_scores:
            if subject_score.midterm_score is not None:
                total_score += subject_score.midterm_score * 1
                total_weight += 1
            if subject_score.final_score is not None:
                total_score += subject_score.final_score * 2
                total_weight += 2
            if subject_score.final_exam_score is not None:
                total_score += subject_score.final_exam_score * 3
                total_weight += 3

        if total_weight > 0:
            return total_score / total_weight
        return None

    def calculate_semester_1_avg(self):
        self.semester_1_avg = self._calculate_avg(semester=1)
        self.is_calculated = True

    def calculate_semester_2_avg(self):
        self.semester_2_avg = self._calculate_avg(semester=2)
        self.is_calculated = True

    def save(self, *args, **kwargs):
        # Check and calculate only if needed
        if not self.pk or not self.is_calculated:
            self.calculate_semester_1_avg()
            self.calculate_semester_2_avg()
        super().save(*args, **kwargs)


