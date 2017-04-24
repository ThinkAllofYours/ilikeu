from django import forms
from .models import Post
from .models import Human


class LoginForm(forms.ModelForm):
    class Meta:
        model = Human
        fields = ('gender', 'mate_date', 'phoneNumber', 'password',)


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'text',)

