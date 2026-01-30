from django.urls import path
from . import views

urlpatterns = [
    path('', views.diet_plans, name='diet_plans'),
    path('plan/<int:plan_id>/', views.diet_plan_detail, name='diet_plan_detail'),
    path('my-diet-plans/', views.my_diet_plans, name='my_diet_plans'),
]