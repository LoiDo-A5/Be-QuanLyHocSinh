from django.contrib import admin

class ClassLevelAdmin(admin.ModelAdmin):
    list_display = ('level_name',)  # Hiển thị tên khối lớp trong danh sách admin
    search_fields = ('level_name',)  # Cho phép tìm kiếm theo tên khối lớp
