from django.contrib import admin

class ClassNameAdmin(admin.ModelAdmin):
    list_display = ('level', 'class_name', 'number_of_students')
    search_fields = ('class_name',)  # Cho phép tìm kiếm theo tên lớp
    list_filter = ('level',)  # Lọc theo khối lớp
