from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import get_user_model
from django.core import serializers
import json
from workouts.models import WorkoutPlan, Exercise, WorkoutSession, WorkoutExercise
from nutrition.models import DietPlan, Food, Meal, MealFood
from calculators.models import BMICalculation, CalorieCalculation
from .forms import (
    UserManagementForm, WorkoutPlanForm, ExerciseForm, 
    DietPlanForm, FoodForm, WorkoutSessionForm
)

User = get_user_model()

def is_admin_user(user):
    return user.is_authenticated and (user.is_superuser or user.role == 'admin')

@login_required
@user_passes_test(is_admin_user)
def admin_dashboard(request):
    # Dashboard statistics
    stats = {
        'total_users': User.objects.count(),
        'active_users': User.objects.filter(is_active_member=True).count(),
        'total_workouts': WorkoutPlan.objects.count(),
        'total_exercises': Exercise.objects.count(),
        'total_diet_plans': DietPlan.objects.count(),
        'total_foods': Food.objects.count(),
        'bmi_calculations': BMICalculation.objects.count(),
        'calorie_calculations': CalorieCalculation.objects.count(),
    }
    
    # Recent activities
    recent_users = User.objects.order_by('-date_joined')[:5]
    recent_workouts = WorkoutPlan.objects.order_by('-created_at')[:5]
    recent_diet_plans = DietPlan.objects.order_by('-created_at')[:5]
    
    # User role distribution - properly formatted for JavaScript
    user_roles_query = User.objects.values('role').annotate(count=Count('role'))
    user_roles = json.dumps(list(user_roles_query))
    
    context = {
        'stats': stats,
        'recent_users': recent_users,
        'recent_workouts': recent_workouts,
        'recent_diet_plans': recent_diet_plans,
        'user_roles': user_roles,
    }
    return render(request, 'admin_panel/dashboard.html', context)

# User Management Views
@login_required
@user_passes_test(is_admin_user)
def user_list(request):
    search_query = request.GET.get('search', '')
    role_filter = request.GET.get('role', '')
    
    users = User.objects.all()
    
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) |
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query)
        )
    
    if role_filter:
        users = users.filter(role=role_filter)
    
    users = users.order_by('-date_joined')
    
    paginator = Paginator(users, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'role_filter': role_filter,
        'user_roles': User.USER_ROLES,
    }
    return render(request, 'admin_panel/user_list.html', context)

@login_required
@user_passes_test(is_admin_user)
def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user_workouts = user.userworkoutplan_set.all()[:5]
    user_diet_plans = user.userdietplan_set.all()[:5]
    bmi_calculations = user.bmicalculation_set.all()[:5]
    calorie_calculations = user.caloriecalculation_set.all()[:5]
    
    context = {
        'user_obj': user,
        'user_workouts': user_workouts,
        'user_diet_plans': user_diet_plans,
        'bmi_calculations': bmi_calculations,
        'calorie_calculations': calorie_calculations,
    }
    return render(request, 'admin_panel/user_detail.html', context)

@login_required
@user_passes_test(is_admin_user)
def user_create(request):
    if request.method == 'POST':
        form = UserManagementForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'User {user.username} created successfully!')
            return redirect('admin_panel:user_detail', user_id=user.id)
    else:
        form = UserManagementForm()
    
    return render(request, 'admin_panel/user_form.html', {'form': form, 'action': 'Create'})

@login_required
@user_passes_test(is_admin_user)
def user_edit(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        form = UserManagementForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, f'User {user.username} updated successfully!')
            return redirect('admin_panel:user_detail', user_id=user.id)
    else:
        form = UserManagementForm(instance=user)
    
    return render(request, 'admin_panel/user_form.html', {
        'form': form, 
        'action': 'Edit', 
        'user_obj': user
    })

@login_required
@user_passes_test(is_admin_user)
@require_http_methods(["POST"])
def user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if user == request.user:
        return JsonResponse({'success': False, 'message': 'Cannot delete your own account'})
    
    username = user.username
    user.delete()
    return JsonResponse({'success': True, 'message': f'User {username} deleted successfully'})

# Workout Management Views
@login_required
@user_passes_test(is_admin_user)
def workout_list(request):
    search_query = request.GET.get('search', '')
    difficulty_filter = request.GET.get('difficulty', '')
    goal_filter = request.GET.get('goal', '')
    
    workouts = WorkoutPlan.objects.all()
    
    if search_query:
        workouts = workouts.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    if difficulty_filter:
        workouts = workouts.filter(difficulty_level=difficulty_filter)
    
    if goal_filter:
        workouts = workouts.filter(goal=goal_filter)
    
    workouts = workouts.order_by('-created_at')
    
    paginator = Paginator(workouts, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'difficulty_filter': difficulty_filter,
        'goal_filter': goal_filter,
    }
    return render(request, 'admin_panel/workout_list.html', context)

@login_required
@user_passes_test(is_admin_user)
def workout_create(request):
    if request.method == 'POST':
        form = WorkoutPlanForm(request.POST)
        if form.is_valid():
            workout = form.save()
            messages.success(request, f'Workout plan "{workout.name}" created successfully!')
            return redirect('admin_panel:workout_detail', workout_id=workout.id)
    else:
        form = WorkoutPlanForm()
    
    return render(request, 'admin_panel/workout_form.html', {'form': form, 'action': 'Create'})

@login_required
@user_passes_test(is_admin_user)
def workout_detail(request, workout_id):
    workout = get_object_or_404(WorkoutPlan, id=workout_id)
    sessions = workout.sessions.all()
    
    # Calculate total exercises
    total_exercises = sum(session.exercises.count() for session in sessions)
    
    context = {
        'workout': workout,
        'sessions': sessions,
        'total_exercises': total_exercises,
    }
    return render(request, 'admin_panel/workout_detail.html', context)

@login_required
@user_passes_test(is_admin_user)
def workout_edit(request, workout_id):
    workout = get_object_or_404(WorkoutPlan, id=workout_id)
    
    if request.method == 'POST':
        form = WorkoutPlanForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            messages.success(request, f'Workout plan "{workout.name}" updated successfully!')
            return redirect('admin_panel:workout_detail', workout_id=workout.id)
    else:
        form = WorkoutPlanForm(instance=workout)
    
    return render(request, 'admin_panel/workout_form.html', {
        'form': form, 
        'action': 'Edit', 
        'workout': workout
    })

@login_required
@user_passes_test(is_admin_user)
@require_http_methods(["POST"])
def workout_delete(request, workout_id):
    workout = get_object_or_404(WorkoutPlan, id=workout_id)
    workout_name = workout.name
    workout.delete()
    return JsonResponse({'success': True, 'message': f'Workout plan "{workout_name}" deleted successfully'})

# Exercise Management Views
@login_required
@user_passes_test(is_admin_user)
def exercise_list(request):
    search_query = request.GET.get('search', '')
    muscle_filter = request.GET.get('muscle_group', '')
    
    exercises = Exercise.objects.all()
    
    if search_query:
        exercises = exercises.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(muscle_groups__icontains=search_query)
        )
    
    if muscle_filter:
        exercises = exercises.filter(muscle_groups__icontains=muscle_filter)
    
    exercises = exercises.order_by('name')
    
    paginator = Paginator(exercises, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get unique muscle groups for filter
    muscle_groups = Exercise.objects.values_list('muscle_groups', flat=True).distinct()
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'muscle_filter': muscle_filter,
        'muscle_groups': muscle_groups,
    }
    return render(request, 'admin_panel/exercise_list.html', context)

@login_required
@user_passes_test(is_admin_user)
def exercise_create(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save()
            messages.success(request, f'Exercise "{exercise.name}" created successfully!')
            return redirect('admin_panel:exercise_list')
    else:
        form = ExerciseForm()
    
    return render(request, 'admin_panel/exercise_form.html', {'form': form, 'action': 'Create'})

@login_required
@user_passes_test(is_admin_user)
def exercise_edit(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id)
    
    if request.method == 'POST':
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            form.save()
            messages.success(request, f'Exercise "{exercise.name}" updated successfully!')
            return redirect('admin_panel:exercise_list')
    else:
        form = ExerciseForm(instance=exercise)
    
    return render(request, 'admin_panel/exercise_form.html', {
        'form': form, 
        'action': 'Edit', 
        'exercise': exercise
    })

@login_required
@user_passes_test(is_admin_user)
@require_http_methods(["POST"])
def exercise_delete(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id)
    exercise_name = exercise.name
    exercise.delete()
    return JsonResponse({'success': True, 'message': f'Exercise "{exercise_name}" deleted successfully'})

# Diet Plan Management Views
@login_required
@user_passes_test(is_admin_user)
def diet_plan_list(request):
    search_query = request.GET.get('search', '')
    goal_filter = request.GET.get('goal', '')
    
    diet_plans = DietPlan.objects.all()
    
    if search_query:
        diet_plans = diet_plans.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    if goal_filter:
        diet_plans = diet_plans.filter(goal=goal_filter)
    
    diet_plans = diet_plans.order_by('-created_at')
    
    paginator = Paginator(diet_plans, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'goal_filter': goal_filter,
    }
    return render(request, 'admin_panel/diet_plan_list.html', context)

@login_required
@user_passes_test(is_admin_user)
def diet_plan_create(request):
    if request.method == 'POST':
        form = DietPlanForm(request.POST)
        if form.is_valid():
            diet_plan = form.save()
            messages.success(request, f'Diet plan "{diet_plan.name}" created successfully!')
            return redirect('admin_panel:diet_plan_list')
    else:
        form = DietPlanForm()
    
    return render(request, 'admin_panel/diet_plan_form.html', {'form': form, 'action': 'Create'})

@login_required
@user_passes_test(is_admin_user)
def diet_plan_edit(request, diet_plan_id):
    diet_plan = get_object_or_404(DietPlan, id=diet_plan_id)
    
    if request.method == 'POST':
        form = DietPlanForm(request.POST, instance=diet_plan)
        if form.is_valid():
            form.save()
            messages.success(request, f'Diet plan "{diet_plan.name}" updated successfully!')
            return redirect('admin_panel:diet_plan_list')
    else:
        form = DietPlanForm(instance=diet_plan)
    
    return render(request, 'admin_panel/diet_plan_form.html', {
        'form': form, 
        'action': 'Edit', 
        'diet_plan': diet_plan
    })

@login_required
@user_passes_test(is_admin_user)
@require_http_methods(["POST"])
def diet_plan_delete(request, diet_plan_id):
    diet_plan = get_object_or_404(DietPlan, id=diet_plan_id)
    diet_plan_name = diet_plan.name
    diet_plan.delete()
    return JsonResponse({'success': True, 'message': f'Diet plan "{diet_plan_name}" deleted successfully'})