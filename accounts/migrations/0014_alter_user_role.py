# Generated by Django 4.2.20 on 2025-04-12 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_systemsetting_max_students_per_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(blank=True, choices=[(1, 'Học sinh'), (2, 'Giáo viên'), (3, 'Quản trị viên')], default=3, null=True),
        ),
    ]
