from django import forms
from .models import Human


class LoginForm(forms.ModelForm):
    class Meta:
        model = Human
        fields = ('gender', 'mate_date', 'phoneNumber', 'password',)


class SaveForm(forms.ModelForm):
    class Meta:
        model = Human
        fields = ('choice1', 'choice2', 'phoneNumber',)
