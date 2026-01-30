from django import forms
from .models import BMICalculation, CalorieCalculation

class BMIForm(forms.ModelForm):
    class Meta:
        model = BMICalculation
        fields = ['height', 'weight']
        widgets = {
            'height': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter height in cm',
                'step': '0.1'
            }),
            'weight': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter weight in kg',
                'step': '0.1'
            }),
        }

class CalorieForm(forms.ModelForm):
    class Meta:
        model = CalorieCalculation
        fields = ['age', 'gender', 'height', 'weight', 'activity_level']
        widgets = {
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter age'
            }),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter height in cm',
                'step': '0.1'
            }),
            'weight': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter weight in kg',
                'step': '0.1'
            }),
            'activity_level': forms.Select(attrs={'class': 'form-control'}),
        }