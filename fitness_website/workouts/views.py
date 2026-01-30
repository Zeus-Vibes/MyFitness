from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import WorkoutPlan, WorkoutSession, Exercise, UserWorkoutPlan

def workout_plans(request):
    plans = WorkoutPlan.objects.all()
    return render(request, 'workouts/workout_plans.html', {'plans': plans})

def workout_plan_detail(request, plan_id):
    plan = get_object_or_404(WorkoutPlan, id=plan_id)
    sessions = plan.sessions.all()
    return render(request, 'workouts/workout_plan_detail.html', {
        'plan': plan,
        'sessions': sessions
    })

def workout_session_detail(request, session_id):
    session = get_object_or_404(WorkoutSession, id=session_id)
    exercises = session.exercises.all()
    return render(request, 'workouts/workout_session_detail.html', {
        'session': session,
        'exercises': exercises
    })

def exercise_detail(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id)
    return render(request, 'workouts/exercise_detail.html', {'exercise': exercise})

def exercises(request):
    exercises = Exercise.objects.all()
    muscle_groups = exercises.values_list('muscle_groups', flat=True).distinct()
    
    # Filter by muscle group if specified
    muscle_filter = request.GET.get('muscle_group')
    if muscle_filter:
        exercises = exercises.filter(muscle_groups__icontains=muscle_filter)
    
    return render(request, 'workouts/exercises.html', {
        'exercises': exercises,
        'muscle_groups': muscle_groups,
        'selected_muscle': muscle_filter
    })

@login_required
def my_workouts(request):
    user_plans = UserWorkoutPlan.objects.filter(user=request.user, is_active=True)
    return render(request, 'workouts/my_workouts.html', {'user_plans': user_plans})