# Generated by Django 4.2.5 on 2023-12-12 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appbanao', '0004_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photos',
            field=models.ImageField(blank=True, default='user-group.svg', null=True, upload_to='images/blog_photos'),
        ),
    ]
