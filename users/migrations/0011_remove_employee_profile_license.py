# Generated by Django 4.1.6 on 2023-03-28 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_employee_profile_agreement_1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_profile',
            name='license',
        ),
    ]