# Generated by Django 3.2.10 on 2022-03-30 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_seller', '0016_rename_asking_pricce_carseller_asking_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carseller',
            name='picture',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
