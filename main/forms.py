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
        exclude = ['user', 'images','is_purchased']

from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
#     captcha = ReCaptchaField()
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', )

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

from django import forms
from .models import BuyModel

class BuyForm(forms.ModelForm):
    class Meta:
        model = BuyModel
        fields = ['card_number', 'expiration_date', 'cvv']
        widgets = {
            'card_number': forms.TextInput(attrs={'placeholder': '0000 0000 0000 0000'}),
            'expiration_date': forms.TextInput(attrs={'placeholder': 'MMYY'}),
            'cvv': forms.TextInput(attrs={'placeholder': 'CVV'}),
        }



# forms.py

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']
