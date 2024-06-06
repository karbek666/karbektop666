from django.contrib.auth.models import User
from django.db import models
class Image_ween(models.Model):
    img = models.ImageField(upload_to='myimge/')
class Ween(models.Model):
    name = models.CharField('Имя', max_length=20)
    images = models.ManyToManyField(Image_ween)
    anons = models.TextField('Добавить описание', max_length=250)
    price = models.IntegerField('Цена', max_length=250)
    number = models.IntegerField("номер-телефона", blank=True, max_length=13)
    date = models.DateTimeField('Дата публикации', auto_now_add=True)
    available_seats = models.IntegerField('Количество комнат', default=10)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Book_list(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Ween, on_delete=models.CASCADE)
    book_data = models.DateTimeField(auto_now_add=True)

class Corzina(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ween = models.ForeignKey(Ween, on_delete=models.CASCADE)

