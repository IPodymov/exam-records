from django import forms
from .models import Exam

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['title', 'date', 'image', 'users', 'is_public']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'users': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
