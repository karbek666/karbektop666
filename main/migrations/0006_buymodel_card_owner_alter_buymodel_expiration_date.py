# Generated by Django 5.0.3 on 2024-07-08 11:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_ween_is_purchased'),
    ]

    operations = [
        migrations.AddField(
            model_name='buymodel',
            name='card_owner',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='buymodel',
            name='expiration_date',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(2024)]),
        ),
    ]
