from django.urls import path
from . import views

urlpatterns = [
    path('bmi/', views.bmi_calculator, name='bmi_calculator'),
    path('calories/', views.calorie_calculator, name='calorie_calculator'),
]