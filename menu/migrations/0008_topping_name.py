# Generated by Django 2.0.3 on 2019-09-13 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_auto_20190910_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='topping',
            name='name',
            field=models.CharField(db_index=True, default=None, max_length=200),
            preserve_default=False,
        ),
    ]