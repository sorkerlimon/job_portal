# Generated by Django 4.1.6 on 2023-03-11 09:20

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_employee_profile_bank_account_employee_profile_dob_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_profile',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]
