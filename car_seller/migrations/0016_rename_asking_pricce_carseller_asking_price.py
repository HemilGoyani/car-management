# Generated by Django 3.2.10 on 2022-03-30 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_seller', '0015_alter_carseller_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carseller',
            old_name='asking_pricce',
            new_name='asking_price',
        ),
    ]
