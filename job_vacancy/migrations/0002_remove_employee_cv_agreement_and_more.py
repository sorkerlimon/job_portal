# Generated by Django 4.1.6 on 2023-02-20 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_vacancy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_cv',
            name='agreement',
        ),
        migrations.RemoveField(
            model_name='employee_cv',
            name='profile_pic',
        ),
    ]
