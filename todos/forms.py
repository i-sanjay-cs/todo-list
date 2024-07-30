# forms.py
from django import forms
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=50,  # Set the maximum length for username
        help_text='Required. 50 characters or fewer. Letters, digits, and @/./+/-/_ only.'
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) > 50:
            raise forms.ValidationError('Username cannot exceed 50 characters.')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username is already taken.')
        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise forms.ValidationError('Password must be at least 8 characters long.')
        if password1.isdigit():
            raise forms.ValidationError('Password cannot be entirely numeric.')
        return password1

class LoginForm(AuthenticationForm):
    pass
