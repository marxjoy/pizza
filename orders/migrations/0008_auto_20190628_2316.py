# Generated by Django 2.0.5 on 2019-06-28 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20190628_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderedpizza',
            name='toppings',
            field=models.ManyToManyField(blank=True, related_name='_orderedpizza_toppings_+', to='orders.OrderedTopping'),
        ),
    ]
