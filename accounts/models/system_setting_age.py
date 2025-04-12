from django.db import models
from django.core.exceptions import ValidationError

class SystemSetting(models.Model):
    min_student_age = models.PositiveIntegerField(default=15)
    max_student_age = models.PositiveIntegerField(default=20)
    max_students_per_class = models.PositiveIntegerField(default=40)
    pass_score = models.FloatField(default=5.0)  # <-- Thêm dòng này

    def save(self, *args, **kwargs):
        if not self.pk and SystemSetting.objects.exists():
            raise ValidationError("Chỉ được phép tạo duy nhất một bản ghi SystemSetting.")
        if self.min_student_age >= self.max_student_age:
            raise ValidationError("Tuổi tối thiểu phải nhỏ hơn tuổi tối đa.")
        if self.max_students_per_class <= 0:
            raise ValidationError("Sĩ số tối đa phải lớn hơn 0.")
        if self.pass_score < 0 or self.pass_score > 10:
            raise ValidationError("Điểm chuẩn phải nằm trong khoảng từ 0 đến 10.")
        super().save(*args, **kwargs)

    def __str__(self):
        return "System Settings"
