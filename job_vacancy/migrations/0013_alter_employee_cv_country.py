# Generated by Django 4.1.6 on 2023-03-28 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_vacancy', '0012_remove_employee_cv_record_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_cv',
            name='country',
            field=models.CharField(blank=True, choices=[('Bangladesh', 'Bangladesh'), ('India', 'India'), ('Srilanka', 'Srilanka'), ('Nepal', 'Nepal'), ('Kenya', 'Kenya')], default='Choose a country', max_length=255, null=True),
        ),
    ]
