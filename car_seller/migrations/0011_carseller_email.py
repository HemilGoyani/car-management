# Generated by Django 3.2.10 on 2022-03-29 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_seller', '0010_carseller_is_sell'),
    ]

    operations = [
        migrations.AddField(
            model_name='carseller',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]