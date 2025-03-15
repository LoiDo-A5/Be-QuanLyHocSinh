from django.contrib import admin

class ClassStudentAdmin(admin.ModelAdmin):
    list_display = ('student', 'class_name')
    search_fields = ('student__full_name', 'class_name__class_name')
    list_filter = ('class_name',)
