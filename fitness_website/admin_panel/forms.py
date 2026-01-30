from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from workouts.models import WorkoutPlan, Exercise, WorkoutSession, WorkoutExercise
from nutrition.models import DietPlan, Food, Meal, MealFood

User = get_user_model()

class UserManagementForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False,
        help_text="Leave blank to keep current password"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False,
        help_text="Confirm new password"
    )
    
    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name', 'role',
            'phone_number', 'date_of_birth', 'age', 'height', 'weight',
            'fitness_goal', 'activity_level', 'is_active', 'is_active_member',
            'membership_start_date'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'fitness_goal': forms.Select(attrs={'class': 'form-control'}),
            'activity_level': forms.Select(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_active_member': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'membership_start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        
        if password:
            user.set_password(password)
        
        if commit:
            user.save()
        return user

class WorkoutPlanForm(forms.ModelForm):
    class Meta:
        model = WorkoutPlan
        fields = ['name', 'description', 'difficulty_level', 'duration_weeks', 'goal']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'difficulty_level': forms.Select(attrs={'class': 'form-control'}),
            'duration_weeks': forms.NumberInput(attrs={'class': 'form-control'}),
            'goal': forms.Select(attrs={'class': 'form-control'}),
        }

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'description', 'muscle_groups', 'equipment_needed', 'youtube_url', 'instructions']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'muscle_groups': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Chest, Shoulders, Triceps'}),
            'equipment_needed': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Dumbbells, Barbell'}),
            'youtube_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://www.youtube.com/watch?v=...'}),
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

class WorkoutSessionForm(forms.ModelForm):
    class Meta:
        model = WorkoutSession
        fields = ['workout_plan', 'name', 'day_number', 'description']
        widgets = {
            'workout_plan': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'day_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class DietPlanForm(forms.ModelForm):
    class Meta:
        model = DietPlan
        fields = ['name', 'description', 'goal', 'daily_calories', 'protein_percentage', 'carbs_percentage', 'fat_percentage']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'goal': forms.Select(attrs={'class': 'form-control'}),
            'daily_calories': forms.NumberInput(attrs={'class': 'form-control'}),
            'protein_percentage': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'max': '100'}),
            'carbs_percentage': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'max': '100'}),
            'fat_percentage': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'max': '100'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        protein = cleaned_data.get('protein_percentage', 0)
        carbs = cleaned_data.get('carbs_percentage', 0)
        fat = cleaned_data.get('fat_percentage', 0)
        
        total = protein + carbs + fat
        if abs(total - 100) > 0.1:  # Allow small floating point differences
            raise forms.ValidationError("Protein, carbs, and fat percentages must add up to 100%")
        
        return cleaned_data

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'calories_per_100g', 'protein_per_100g', 'carbs_per_100g', 'fat_per_100g', 'fiber_per_100g']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'calories_per_100g': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'protein_per_100g': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'carbs_per_100g': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'fat_per_100g': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'fiber_per_100g': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
        }