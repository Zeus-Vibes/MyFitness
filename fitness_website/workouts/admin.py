from django.contrib import admin
from .models import WorkoutPlan, Exercise, WorkoutSession, WorkoutExercise, UserWorkoutPlan

class WorkoutExerciseInline(admin.TabularInline):
    model = WorkoutExercise
    extra = 1

class WorkoutSessionInline(admin.TabularInline):
    model = WorkoutSession
    extra = 1

@admin.register(WorkoutPlan)
class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'difficulty_level', 'goal', 'duration_weeks', 'created_at']
    list_filter = ['difficulty_level', 'goal', 'created_at']
    search_fields = ['name', 'description']
    inlines = [WorkoutSessionInline]

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['name', 'muscle_groups', 'equipment_needed']
    list_filter = ['muscle_groups']
    search_fields = ['name', 'muscle_groups']

@admin.register(WorkoutSession)
class WorkoutSessionAdmin(admin.ModelAdmin):
    list_display = ['name', 'workout_plan', 'day_number']
    list_filter = ['workout_plan']
    inlines = [WorkoutExerciseInline]

@admin.register(UserWorkoutPlan)
class UserWorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ['user', 'workout_plan', 'start_date', 'is_active', 'completed']
    list_filter = ['is_active', 'completed', 'start_date']