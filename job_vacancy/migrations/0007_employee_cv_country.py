# Generated by Django 4.1.6 on 2023-03-17 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_vacancy', '0006_alter_employee_cv_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_cv',
            name='country',
            field=models.CharField(blank=True, choices=[('Bangladesh', 'Bangladesh'), ('India', 'India'), ('Srilanka', 'Srilanka'), ('Nepal', 'Nepal'), ('Kenya', 'Kenya')], default='', max_length=255, null=True),
        ),
    ]
