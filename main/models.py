from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.utils import timezone


class Image_ween(models.Model):
    img = models.ImageField(',', upload_to='myimge/')
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
class Ween(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Имя', max_length=20)
    images = models.ManyToManyField(Image_ween)
    anons = models.TextField('Добавить описание', max_length=250)
    price = models.IntegerField('Цена', max_length=250)
    number = models.IntegerField("номер-телефона", blank=True, max_length=13)
    date = models.DateTimeField('Дата публикации', auto_now_add=True)
    available_seats = models.IntegerField('Количество комнат', default=10)
    image = models.ImageField('Лицевое фото')
    is_purchased = models.BooleanField(default=False)  # Новое поле
    def __str__(self):
        return self.name


class Book_list(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Ween, on_delete=models.CASCADE)
    book_data = models.DateTimeField(auto_now_add=True)
    is_purchased = models.BooleanField(default=False)  # Новое поле

class Corzina(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ween = models.ForeignKey(Ween, on_delete=models.CASCADE)

class BuyModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.OneToOneField(Book_list, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    card_number = models.CharField(max_length=16, validators=[MinLengthValidator(16)])
    expiration_date = models.IntegerField(validators=[MinValueValidator(2024)])
    cvv = models.CharField(max_length=3)
    card_owner = models.CharField(max_length=100)
    payment_date = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)