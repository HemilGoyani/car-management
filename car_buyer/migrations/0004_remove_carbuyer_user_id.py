# Generated by Django 3.2.10 on 2022-03-30 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_buyer', '0003_auto_20220330_0852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carbuyer',
            name='user_id',
        ),
    ]
