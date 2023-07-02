"""
    Admin for the custom user and Event.

    Event Mangement, 2023

    Author: Jay Chovatiya
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Event

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'is_staff']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    # Defaul user model ordring by username, but we cann't username in custom user model
    ordering = ('email',)


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_datetime', 'end_datetime', 'location', 'user']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Event, EventAdmin)
