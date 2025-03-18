from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin


class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'full_name', 'email', 'phone_number', 'first_name', 'last_name', 'avatar',
                    'birthday', 'is_phone_verified', 'role', 'age')

    list_filter = ('role', 'full_name', 'email', 'is_phone_verified')

    search_fields = ('full_name', 'email', 'phone_number', 'birthday', 'role')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info',
         {'fields': ('full_name', 'first_name', 'last_name', 'phone_number', 'birthday', 'gender', 'address')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Custom Fields', {'fields': ('avatar', 'is_phone_verified', 'time_zone', 'role')}),
    )

    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'password1', 'password2')}),
        ('Personal Info',
         {'fields': ('full_name', 'first_name', 'last_name', 'phone_number', 'birthday', 'gender', 'address')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Custom Fields', {'fields': ('avatar', 'is_phone_verified', 'time_zone', 'role')}),
    )
