# Generated by Django 2.0.3 on 2019-07-10 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0022_orderedmeal_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderedmeal',
            name='sub_toppings',
            field=models.ManyToManyField(blank=True, to='orders.SubTopping'),
        ),
    ]