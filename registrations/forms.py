from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'registration_number': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'vit_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'hostel': forms.Select(attrs={'class': 'form-control'}),
            'room_number': forms.TextInput(attrs={'class': 'form-control'}),
            'game_playing': forms.Select(attrs={'class': 'form-control'}),
        }
