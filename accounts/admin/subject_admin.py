from django.contrib import admin

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')

    search_fields = ('name', 'code')

    list_filter = ('name',)
