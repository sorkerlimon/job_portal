# Generated by Django 4.1.6 on 2023-03-07 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_vacancy', '0005_employee_cv_meet_link_sent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_cv',
            name='cv',
            field=models.FileField(upload_to='cv/'),
        ),
    ]
