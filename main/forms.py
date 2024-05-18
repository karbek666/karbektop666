from django import forms
from django.forms import ModelForm
from django_recaptcha.fields import ReCaptchaField
from django.contrib.auth.models import User
from .models import Ween


class SampleModelForm(ModelForm):
    class Meta:
        model = Ween
        fields='__all__'

from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
#     captcha = ReCaptchaField()
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', )

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

