# Generated by Django 4.1.6 on 2023-03-21 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_vacancy', '0008_employee_cv_record_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_cv',
            name='record_number',
        ),
    ]
