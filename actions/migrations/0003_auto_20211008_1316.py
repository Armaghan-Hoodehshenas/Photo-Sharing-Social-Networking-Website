# Generated by Django 3.1.6 on 2021-10-08 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('actions', '0002_auto_20211008_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='target_ct',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='target_obj', to='contenttypes.contenttype', verbose_name='آبجکت هدف'),
        ),
        migrations.AlterField(
            model_name='action',
            name='target_id',
            field=models.PositiveIntegerField(blank=True, db_index=True, null=True, verbose_name='آی دی هدف'),
        ),
    ]