# Generated by Django 4.1.6 on 2023-03-28 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_vacancy', '0015_employee_cv_interestedfor_employee_cv_position_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_cv',
            name='startingdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]