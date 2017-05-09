from django import forms
from .models import Human
from .models import MateDates
from django import forms


class LoginForm(forms.ModelForm):
    class Meta:
        model = Human
        fields = ('gender', 'mate_date', 'phoneNumber', 'password',)


class SaveForm(forms.ModelForm):
    class Meta:
        model = Human
        fields = ('choice1', 'choice2', 'phoneNumber',)


class DateForm(forms.ModelForm):
    class Meta:
        model = MateDates
        fields = ('mate_date', "start_choice", "end_choice",)