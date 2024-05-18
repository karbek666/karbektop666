from django.contrib.auth.models import User
from django.db import models

class Ween(models.Model):
    name = models.CharField('Имя', max_length=20)
    anons = models.CharField('Добавить описание', max_length=250)
    price = models.CharField('Цена', max_length=250)
    image = models.ImageField(blank=True, upload_to='images/')
    date = models.DateTimeField('Дата публикации')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Book_list(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Ween, on_delete=models.CASCADE)
    book_data = models.DateTimeField(auto_now_add=True)