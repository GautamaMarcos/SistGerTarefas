from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['nome', 'descricao', 'status']
        widgets = {
            'nome': forms.TextInput(attrs={'required': False}),
        }