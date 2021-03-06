from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.contrib.auth.models import User


class AuthUserForm(UserCreationForm):
    email = forms.EmailField()
    adress = forms.CharField()
    namesunname = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'namesunname', 'adress', 'password1', 'password2']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Логин"
        self.fields['password'].label = "Пароль"

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(f"Пользователь с логином {username} не найден.")
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError("неверный пароль")
        return self.cleaned_data


class OrderForm(forms.Form):
    amount = forms.IntegerField(label="Quantity")
