# Generated by Django 4.1.6 on 2023-02-21 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_user_employee_profile_u_user'),
        ('job_vacancy', '0003_rename_user_employee_cv_p_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_cv',
            name='p_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.employee_profile'),
        ),
    ]
