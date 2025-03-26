from django.db import models

class ClassLevel(models.Model):
    level_name = models.CharField(max_length=10, unique=True)  # Khối lớp (10, 11, 12)

    def __str__(self):
        return self.level_name
