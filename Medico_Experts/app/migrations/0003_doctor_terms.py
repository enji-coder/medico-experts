# Generated by Django 2.2.6 on 2019-11-07 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191018_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='terms',
            field=models.BooleanField(default=False),
        ),
    ]
