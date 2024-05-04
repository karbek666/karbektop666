from django import forms
from django.forms import ModelForm
from django_recaptcha.fields import ReCaptchaField

from .models import ween


class SampleModelForm(ModelForm):
    class Meta:
        model = ween
        fields='__all__'

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class RegisterForm(UserCreationForm):
    captcha = ReCaptchaField()
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'captcha')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = ReCaptchaField()