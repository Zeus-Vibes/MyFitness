from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class DietPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    goal = models.CharField(
        max_length=50,
        choices=[
            ('weight_loss', 'Weight Loss'),
            ('muscle_gain', 'Muscle Gain'),
            ('maintenance', 'Maintenance'),
        ]
    )
    daily_calories = models.PositiveIntegerField()
    protein_percentage = models.FloatField()
    carbs_percentage = models.FloatField()
    fat_percentage = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=100)
    calories_per_100g = models.FloatField()
    protein_per_100g = models.FloatField()
    carbs_per_100g = models.FloatField()
    fat_per_100g = models.FloatField()
    fiber_per_100g = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Meal(models.Model):
    MEAL_TYPES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ]
    
    diet_plan = models.ForeignKey(DietPlan, on_delete=models.CASCADE, related_name='meals')
    meal_type = models.CharField(max_length=20, choices=MEAL_TYPES)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.diet_plan.name} - {self.get_meal_type_display()}: {self.name}"

class MealFood(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='foods')
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity_grams = models.FloatField()

    def __str__(self):
        return f"{self.food.name} - {self.quantity_grams}g"

    @property
    def calories(self):
        return (self.food.calories_per_100g * self.quantity_grams) / 100

    @property
    def protein(self):
        return (self.food.protein_per_100g * self.quantity_grams) / 100

    @property
    def carbs(self):
        return (self.food.carbs_per_100g * self.quantity_grams) / 100

    @property
    def fat(self):
        return (self.food.fat_per_100g * self.quantity_grams) / 100

class UserDietPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    diet_plan = models.ForeignKey(DietPlan, on_delete=models.CASCADE)
    start_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.diet_plan.name}"