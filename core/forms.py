from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Seu Nome',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Sua senha',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))


class CadastroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Seu Nome',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Seu E-mail',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Sua Senha',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Digite sua senha novamente',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))