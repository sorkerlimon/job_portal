# Generated by Django 4.1.6 on 2023-03-21 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_vacancy', '0009_remove_employee_cv_record_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_cv',
            name='record_number',
            field=models.IntegerField(default=0),
        ),
    ]
