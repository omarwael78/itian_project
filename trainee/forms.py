from django import forms
from .models import Trainee

class TraineeModelForm(forms.ModelForm):
    class Meta:
        model = Trainee
        fields = ['name', 'course', 'personal_image']
        
        labels = {
            'name': 'Full Name',
            'course': 'Select Course',
            'personal_image': 'Profile Picture',
        }
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'personal_image': forms.FileInput(attrs={'class': 'form-control'}),
        }