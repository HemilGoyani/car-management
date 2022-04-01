# Generated by Django 3.2.10 on 2022-04-01 07:14

from django.db import migrations
import djmoney.models.fields
import djmoney.models.validators


class Migration(migrations.Migration):

    dependencies = [
        ('car_seller', '0022_alter_carseller_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carseller',
            name='asking_price',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='USD', max_digits=8, validators=[djmoney.models.validators.MinMoneyValidator(1000), djmoney.models.validators.MaxMoneyValidator(100000)]),
        ),
    ]
