# Generated by Django 4.1.6 on 2023-03-08 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_u_user_employee_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_profile',
            name='has_used_secret_key',
            field=models.BooleanField(default=False),
        ),
    ]
