# Generated by Django 3.2.10 on 2022-04-01 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_buyer', '0003_alter_carbuyer_make'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carbuyer',
            name='Condition',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='carbuyer',
            name='model',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='carbuyer',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
