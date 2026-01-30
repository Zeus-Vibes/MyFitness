from django.contrib import admin
from .models import BMICalculation, CalorieCalculation

@admin.register(BMICalculation)
class BMICalculationAdmin(admin.ModelAdmin):
    list_display = ['user', 'height', 'weight', 'bmi', 'category', 'calculated_at']
    list_filter = ['category', 'calculated_at']
    readonly_fields = ['bmi', 'category']

@admin.register(CalorieCalculation)
class CalorieCalculationAdmin(admin.ModelAdmin):
    list_display = ['user', 'age', 'gender', 'activity_level', 'bmr', 'tdee', 'calculated_at']
    list_filter = ['gender', 'activity_level', 'calculated_at']
    readonly_fields = ['bmr', 'tdee']