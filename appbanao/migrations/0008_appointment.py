# Generated by Django 4.2.5 on 2024-01-05 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appbanao', '0007_alter_user_profile_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speciality', models.CharField(max_length=200)),
                ('start_time', models.DateField()),
                ('end_time', models.TimeField()),
            ],
        ),
    ]
