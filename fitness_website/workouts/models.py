from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class WorkoutPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty_level = models.CharField(
        max_length=20,
        choices=[
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced'),
        ]
    )
    duration_weeks = models.PositiveIntegerField()
    goal = models.CharField(
        max_length=50,
        choices=[
            ('weight_loss', 'Weight Loss'),
            ('muscle_gain', 'Muscle Gain'),
            ('strength', 'Strength'),
            ('endurance', 'Endurance'),
        ]
    )
    image = models.ImageField(upload_to='workout_plans/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    muscle_groups = models.CharField(max_length=200)
    equipment_needed = models.CharField(max_length=200, blank=True)
    youtube_url = models.URLField(blank=True, help_text="YouTube video URL for exercise demonstration")
    image = models.ImageField(upload_to='exercises/', blank=True, null=True)
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class WorkoutSession(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='sessions')
    name = models.CharField(max_length=100)
    day_number = models.PositiveIntegerField()
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['day_number']

    def __str__(self):
        return f"{self.workout_plan.name} - Day {self.day_number}: {self.name}"

class WorkoutExercise(models.Model):
    session = models.ForeignKey(WorkoutSession, on_delete=models.CASCADE, related_name='exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField()
    reps = models.CharField(max_length=50, help_text="e.g., '12', '8-10', '30 seconds'")
    rest_time = models.CharField(max_length=50, help_text="Rest time between sets")
    notes = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.exercise.name} - {self.sets}x{self.reps}"

class UserWorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    start_date = models.DateField()
    is_active = models.BooleanField(default=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.workout_plan.name}"