# Generated by Django 4.1.6 on 2023-02-21 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_employee_profile_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee_profile',
            old_name='user',
            new_name='u_user',
        ),
    ]