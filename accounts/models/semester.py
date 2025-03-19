from django.db import models

class Semester(models.Model):
    SEMESTER_CHOICES = [
        (1, 'Học kỳ 1'),
        (2, 'Học kỳ 2'),
    ]
    semester = models.IntegerField(choices=SEMESTER_CHOICES)

    def __str__(self):
        return dict(self.SEMESTER_CHOICES).get(self.semester)
