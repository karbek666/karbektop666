from django.db import models

class ween(models.Model):
    name = models.CharField('Имя', max_length=20)
    anons = models.CharField('Добавить описание', max_length=250)
    price = models.CharField('Цена', max_length=250)
    image = models.ImageField(blank=True, upload_to='images')
    date = models.DateTimeField('Дата публикации')



