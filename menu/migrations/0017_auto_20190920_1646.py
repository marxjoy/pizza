# Generated by Django 2.0.3 on 2019-09-20 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0016_auto_20190920_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='category',
            field=models.CharField(default='object', max_length=100),
        ),
    ]