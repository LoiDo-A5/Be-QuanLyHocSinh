from django.contrib import admin

class StudentScoreAdmin(admin.ModelAdmin):
    list_display = ('student', 'class_name', 'semester_1_avg', 'semester_2_avg')
    search_fields = ('student__full_name', 'class_name__class_name')

    list_filter = ('class_name', 'student')

    fieldsets = (
        (None, {
            'fields': ('student', 'class_name')
        }),
        ('Điểm học kỳ', {
            'fields': ('semester_1_avg', 'semester_2_avg')
        }),
    )

    class Meta:
        unique_together = ['student', 'class_name']