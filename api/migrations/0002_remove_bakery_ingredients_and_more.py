# Generated by Django 4.0.2 on 2022-12-11 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bakery',
            name='Ingredients',
        ),
        migrations.RemoveField(
            model_name='bakery',
            name='Ingredients_quantity',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]
