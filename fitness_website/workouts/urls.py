from django.urls import path
from . import views

urlpatterns = [
    path('', views.workout_plans, name='workout_plans'),
    path('plan/<int:plan_id>/', views.workout_plan_detail, name='workout_plan_detail'),
    path('session/<int:session_id>/', views.workout_session_detail, name='workout_session_detail'),
    path('exercise/<int:exercise_id>/', views.exercise_detail, name='exercise_detail'),
    path('exercises/', views.exercises, name='exercises'),
    path('my-workouts/', views.my_workouts, name='my_workouts'),
]