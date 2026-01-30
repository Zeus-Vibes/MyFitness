from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'role', 'is_active_member', 'is_staff']
    list_filter = ['role', 'is_active_member', 'fitness_goal', 'activity_level', 'date_joined']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    
    fieldsets = UserAdmin.fieldsets + (
        ('Role & Membership', {
            'fields': ('role', 'is_active_member', 'membership_start_date')
        }),
        ('Personal Information', {
            'fields': ('phone_number', 'date_of_birth', 'profile_picture')
        }),
        ('Fitness Information', {
            'fields': ('age', 'height', 'weight', 'fitness_goal', 'activity_level')
        }),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Role & Membership', {
            'fields': ('role', 'is_active_member', 'membership_start_date')
        }),
        ('Personal Information', {
            'fields': ('phone_number', 'date_of_birth', 'profile_picture')
        }),
        ('Fitness Information', {
            'fields': ('age', 'height', 'weight', 'fitness_goal', 'activity_level')
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)