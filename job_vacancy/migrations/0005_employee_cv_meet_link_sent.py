# Generated by Django 4.1.6 on 2023-03-06 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_vacancy', '0004_alter_employee_cv_p_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_cv',
            name='meet_link_sent',
            field=models.BooleanField(default=False),
        ),
    ]
