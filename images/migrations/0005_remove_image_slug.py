# Generated by Django 3.1.6 on 2021-09-28 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_remove_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='slug',
        ),
    ]
