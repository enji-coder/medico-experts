# Generated by Django 2.2.6 on 2019-11-13 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_doctor_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]