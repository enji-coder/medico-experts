# Generated by Django 2.2.6 on 2019-11-14 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_doctor_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.FileField(blank=True, default='app/images/doc.png', upload_to='medico_experts/images/')),
                ('firstname', models.CharField(blank=True, max_length=50)),
                ('lastname', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(blank=True, max_length=10)),
                ('contactno', models.CharField(blank=True, max_length=10)),
                ('terms', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
        ),
    ]
