# Generated by Django 2.0.3 on 2019-09-20 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0014_auto_20190920_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='category',
            field=models.CharField(default='%(app_label)s_%(class)ss', max_length=100),
        ),
    ]