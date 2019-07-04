# Generated by Django 2.0.5 on 2019-06-29 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20190628_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='category',
            field=models.CharField(choices=[('Regular', 'Regular Pizza'), ('Sicilian', 'Sicilian Pizza'), ('Salad', 'Salad'), ('Pasta', 'Pasta'), ('Subs', 'Subs'), ('Dinner', 'Dinner Platters')], default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pizza',
            name='size',
            field=models.CharField(choices=[('L', 'Large'), ('M', 'Medium'), ('S', 'Small')], default='1', max_length=10),
            preserve_default=False,
        ),
    ]
