# Generated by Django 2.0.3 on 2019-09-20 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0019_auto_20190920_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='price',
        ),
        migrations.AddField(
            model_name='meal',
            name='price_s',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='price for Small meal if exists'),
        ),
    ]