from django import forms
from .models import Post
from .models import Man
from .models import Woman

class PostForm(forms.ModelForm):
    
    class Meta :
        model = Post
        fields = ('title', 'text',)

    class Man :
        model = Man
        fields = ('gender', 'mate_date', 'phone_number', 'number', 'password',)

    class Woman :
        model = Woman
        fields = ('gender', 'mate_date', 'phone_number', 'number', 'password',)