from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DietPlan, UserDietPlan

def diet_plans(request):
    plans = DietPlan.objects.all()
    return render(request, 'nutrition/diet_plans.html', {'plans': plans})

def diet_plan_detail(request, plan_id):
    plan = get_object_or_404(DietPlan, id=plan_id)
    meals = plan.meals.all()
    
    # Group meals by type
    meals_by_type = {}
    for meal in meals:
        if meal.meal_type not in meals_by_type:
            meals_by_type[meal.meal_type] = []
        meals_by_type[meal.meal_type].append(meal)
    
    return render(request, 'nutrition/diet_plan_detail.html', {
        'plan': plan,
        'meals_by_type': meals_by_type
    })

@login_required
def my_diet_plans(request):
    user_plans = UserDietPlan.objects.filter(user=request.user, is_active=True)
    return render(request, 'nutrition/my_diet_plans.html', {'user_plans': user_plans})