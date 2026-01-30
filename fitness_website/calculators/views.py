from django.shortcuts import render
from django.contrib import messages
from .models import BMICalculation, CalorieCalculation
from .forms import BMIForm, CalorieForm

def bmi_calculator(request):
    result = None
    if request.method == 'POST':
        form = BMIForm(request.POST)
        if form.is_valid():
            bmi_calc = form.save(commit=False)
            if request.user.is_authenticated:
                bmi_calc.user = request.user
            bmi_calc.save()
            result = bmi_calc
            messages.success(request, 'BMI calculated successfully!')
    else:
        form = BMIForm()
        # Pre-fill with user data if available
        if request.user.is_authenticated and request.user.height and request.user.weight:
            form.initial = {
                'height': request.user.height,
                'weight': request.user.weight
            }
    
    return render(request, 'calculators/bmi_calculator.html', {
        'form': form,
        'result': result
    })

def calorie_calculator(request):
    result = None
    if request.method == 'POST':
        form = CalorieForm(request.POST)
        if form.is_valid():
            calorie_calc = form.save(commit=False)
            if request.user.is_authenticated:
                calorie_calc.user = request.user
            calorie_calc.save()
            result = calorie_calc
            messages.success(request, 'Daily calorie needs calculated successfully!')
    else:
        form = CalorieForm()
        # Pre-fill with user data if available
        if request.user.is_authenticated:
            initial_data = {}
            if request.user.age:
                initial_data['age'] = request.user.age
            if request.user.height:
                initial_data['height'] = request.user.height
            if request.user.weight:
                initial_data['weight'] = request.user.weight
            if request.user.activity_level:
                initial_data['activity_level'] = request.user.activity_level
            form.initial = initial_data
    
    return render(request, 'calculators/calorie_calculator.html', {
        'form': form,
        'result': result
    })