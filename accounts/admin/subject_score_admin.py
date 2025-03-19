from django.contrib import admin

class SubjectScoreAdmin(admin.ModelAdmin):
    list_display = ('student', 'class_name', 'subject', 'semester', 'midterm_score', 'final_score', 'final_exam_score')
    search_fields = ('student__full_name', 'class_name__class_name', 'subject__name')
    list_filter = ('semester', 'class_name', 'subject')

    fieldsets = (
        (None, {
            'fields': ('student', 'class_name', 'subject', 'semester')
        }),
        ('Điểm học kỳ', {
            'fields': ('midterm_score', 'final_score', 'final_exam_score')
        }),
    )

    class Meta:
        unique_together = ['student', 'subject', 'class_name', 'semester']

