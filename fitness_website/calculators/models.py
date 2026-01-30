from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class BMICalculation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    height = models.FloatField(help_text="Height in cm")
    weight = models.FloatField(help_text="Weight in kg")
    bmi = models.FloatField()
    category = models.CharField(max_length=50)
    calculated_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Calculate BMI
        height_m = self.height / 100
        self.bmi = round(self.weight / (height_m ** 2), 2)
        
        # Determine category
        if self.bmi < 18.5:
            self.category = "Underweight"
        elif 18.5 <= self.bmi < 25:
            self.category = "Normal weight"
        elif 25 <= self.bmi < 30:
            self.category = "Overweight"
        else:
            self.category = "Obese"
            
        super().save(*args, **kwargs)

    def __str__(self):
        return f"BMI: {self.bmi} ({self.category})"

class CalorieCalculation(models.Model):
    ACTIVITY_MULTIPLIERS = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'extra_active': 1.9,
    }

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    height = models.FloatField(help_text="Height in cm")
    weight = models.FloatField(help_text="Weight in kg")
    activity_level = models.CharField(
        max_length=20,
        choices=[
            ('sedentary', 'Sedentary'),
            ('light', 'Light Activity'),
            ('moderate', 'Moderate Activity'),
            ('active', 'Very Active'),
            ('extra_active', 'Extra Active'),
        ]
    )
    bmr = models.FloatField()
    tdee = models.FloatField()
    calculated_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Calculate BMR using Mifflin-St Jeor Equation
        if self.gender == 'male':
            self.bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        else:
            self.bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age - 161
        
        # Calculate TDEE
        multiplier = self.ACTIVITY_MULTIPLIERS.get(self.activity_level, 1.2)
        self.tdee = round(self.bmr * multiplier, 0)
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"TDEE: {self.tdee} calories/day"