# Generated by Django 4.2.20 on 2025-04-05 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_systemsetting'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemsetting',
            name='max_students_per_class',
            field=models.PositiveIntegerField(default=40),
        ),
    ]
