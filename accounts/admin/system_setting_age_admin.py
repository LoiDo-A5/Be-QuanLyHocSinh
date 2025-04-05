from django.contrib import admin

class SystemSettingAdmin(admin.ModelAdmin):
    list_display = ('min_student_age', 'max_student_age')
    search_fields = ('min_student_age', 'max_student_age')
    list_filter = ('min_student_age', 'max_student_age')
