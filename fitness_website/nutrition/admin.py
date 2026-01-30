from django.contrib import admin
from .models import DietPlan, Food, Meal, MealFood, UserDietPlan

class MealFoodInline(admin.TabularInline):
    model = MealFood
    extra = 1

class MealInline(admin.TabularInline):
    model = Meal
    extra = 1

@admin.register(DietPlan)
class DietPlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'goal', 'daily_calories', 'created_at']
    list_filter = ['goal', 'created_at']
    search_fields = ['name', 'description']
    inlines = [MealInline]

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'calories_per_100g', 'protein_per_100g', 'carbs_per_100g', 'fat_per_100g']
    search_fields = ['name']

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ['name', 'diet_plan', 'meal_type']
    list_filter = ['meal_type', 'diet_plan']
    inlines = [MealFoodInline]

@admin.register(UserDietPlan)
class UserDietPlanAdmin(admin.ModelAdmin):
    list_display = ['user', 'diet_plan', 'start_date', 'is_active']
    list_filter = ['is_active', 'start_date']