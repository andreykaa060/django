from django import forms
from .models import *


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'name-input',
                'placeholder': 'Имя'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'input-phone form-control',
                'id': 'phone-input',
                'placeholder': 'Телефон'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'message-input',
                'placeholder': 'Сообщение',
                'rows': '3'
            }),
        }
