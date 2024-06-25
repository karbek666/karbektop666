from django import forms
from django.forms import ModelForm
from django_recaptcha.fields import ReCaptchaField
from django.contrib.auth.models import User
from .models import Ween, Image_ween, BuyModel, Message


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image_ween
        fields = ('img', )
class SampleModelForm(ModelForm):
    class Meta:
        model = Ween
        fields='__all__'
        exclude = ['author', 'images']

from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
#     captcha = ReCaptchaField()
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', )

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class BuyForm(forms.ModelForm):
    card_number = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер карты'}))
    expiration_date = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Год'}))
    cvv = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'CVC'}))
    class Meta:
        model = BuyModel
        fields = ['card_number', 'expiration_date', 'cvv']


# forms.py

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']
