# Generated by Django 4.2.6 on 2025-03-19 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_classlevel_classname_classstudent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField(choices=[(1, 'Học kỳ 1'), (2, 'Học kỳ 2')])),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('midterm_score', models.FloatField(blank=True, null=True)),
                ('final_score', models.FloatField(blank=True, null=True)),
                ('final_exam_score', models.FloatField(blank=True, null=True)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.classname')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.semester')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.subject')),
            ],
            options={
                'unique_together': {('student', 'subject', 'class_name', 'semester')},
            },
        ),
        migrations.CreateModel(
            name='StudentScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_1_avg', models.FloatField(blank=True, null=True)),
                ('semester_2_avg', models.FloatField(blank=True, null=True)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.classname')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('student', 'class_name')},
            },
        ),
    ]
