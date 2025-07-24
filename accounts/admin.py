from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.urls import reverse
from django.utils.html import format_html

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('name', 'email', 'username', 'is_active', 'is_staff', 'created_at', 'updated_at')
    search_fields = ('username', 'email', 'name')
    list_filter = ('is_active', 'is_staff')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'name', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at'), 'classes': ('collapse',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'name', 'email', 'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )

    def change_password_link(self, obj):
        url = reverse('admin:auth_user_password_change', args=[obj.pk])
        return format_html('<a href="{}">Change password</a>', url)

    change_password_link.short_description = 'Change password'
