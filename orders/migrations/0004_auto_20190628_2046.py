# Generated by Django 2.0.5 on 2019-06-28 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20190628_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='toppings',
        ),
        migrations.AddField(
            model_name='orderedpizza',
            name='toppings',
            field=models.ManyToManyField(blank=True, to='orders.Topping'),
        ),
    ]