from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_ROLES = [
        ('user', 'Regular User'),
        ('trainer', 'Trainer'),
        ('admin', 'Administrator'),
    ]
    
    role = models.CharField(max_length=20, choices=USER_ROLES, default='user')
    age = models.PositiveIntegerField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True, help_text="Height in cm")
    weight = models.FloatField(null=True, blank=True, help_text="Weight in kg")
    fitness_goal = models.CharField(
        max_length=50,
        choices=[
            ('weight_loss', 'Weight Loss'),
            ('muscle_gain', 'Muscle Gain'),
            ('maintenance', 'Maintenance'),
            ('endurance', 'Endurance'),
        ],
        null=True,
        blank=True
    )
    activity_level = models.CharField(
        max_length=20,
        choices=[
            ('sedentary', 'Sedentary'),
            ('light', 'Light Activity'),
            ('moderate', 'Moderate Activity'),
            ('active', 'Very Active'),
            ('extra_active', 'Extra Active'),
        ],
        null=True,
        blank=True
    )
    phone_number = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    is_active_member = models.BooleanField(default=True)
    membership_start_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    
    @property
    def is_admin_user(self):
        return self.role == 'admin' or self.is_superuser
    
    @property
    def is_trainer(self):
        return self.role == 'trainer'
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip() or self.username