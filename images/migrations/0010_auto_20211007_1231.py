# Generated by Django 3.1.6 on 2021-10-07 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0009_auto_20211001_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, verbose_name='اسلاگ'),
        ),
    ]