# Generated by Django 2.0.3 on 2019-09-20 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0013_meal_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='category',
            field=models.CharField(default='%(app_label)s_%(class)s', max_length=100),
        ),
    ]