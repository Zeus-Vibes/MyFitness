from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    # Dashboard
    path('', views.admin_dashboard, name='dashboard'),
    
    # User Management
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('users/<int:user_id>/edit/', views.user_edit, name='user_edit'),
    path('users/<int:user_id>/delete/', views.user_delete, name='user_delete'),
    
    # Workout Management
    path('workouts/', views.workout_list, name='workout_list'),
    path('workouts/create/', views.workout_create, name='workout_create'),
    path('workouts/<int:workout_id>/', views.workout_detail, name='workout_detail'),
    path('workouts/<int:workout_id>/edit/', views.workout_edit, name='workout_edit'),
    path('workouts/<int:workout_id>/delete/', views.workout_delete, name='workout_delete'),
    
    # Exercise Management
    path('exercises/', views.exercise_list, name='exercise_list'),
    path('exercises/create/', views.exercise_create, name='exercise_create'),
    path('exercises/<int:exercise_id>/edit/', views.exercise_edit, name='exercise_edit'),
    path('exercises/<int:exercise_id>/delete/', views.exercise_delete, name='exercise_delete'),
    
    # Diet Plan Management
    path('diet-plans/', views.diet_plan_list, name='diet_plan_list'),
    path('diet-plans/create/', views.diet_plan_create, name='diet_plan_create'),
    path('diet-plans/<int:diet_plan_id>/edit/', views.diet_plan_edit, name='diet_plan_edit'),
    path('diet-plans/<int:diet_plan_id>/delete/', views.diet_plan_delete, name='diet_plan_delete'),
]