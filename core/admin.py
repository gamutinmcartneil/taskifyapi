"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['username', 'joined','email']
    readonly_fields = ['joined', 'last_login']  # Make 'joined' and 'last_login' read-only

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('username Info'), {'fields': ('first_name', 'middle_name', 'last_name', 'email')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Joined'), {'fields': ('joined',)}),  # Include 'joined' in a read-only manner
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'password1',
                'password2',
                'first_name',
                'middle_name',
                'last_name',
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
    )

admin.site.register(models.User, UserAdmin)

