# Generated by Django 2.0.3 on 2019-09-23 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20190923_1053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='meal_description',
            new_name='meal',
        ),
    ]
