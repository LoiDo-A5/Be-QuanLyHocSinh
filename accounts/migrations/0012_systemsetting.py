# Generated by Django 4.2.20 on 2025-03-29 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_studentscore_unique_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_student_age', models.PositiveIntegerField(default=15)),
                ('max_student_age', models.PositiveIntegerField(default=20)),
            ],
        ),
    ]
