# Generated by Django 4.1.6 on 2023-03-28 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_vacancy', '0016_alter_employee_cv_startingdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_cv',
            name='agreementlicens',
            field=models.BooleanField(default=False),
        ),
    ]
