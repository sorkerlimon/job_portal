# Generated by Django 4.1.6 on 2023-03-11 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_employee_profile_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_profile',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employee_profile',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee_profile',
            name='education_degree',
            field=models.CharField(blank=True, choices=[('Completed 10 years school', 'Completed 10 years school'), ('Completed 10 years school & High School', 'Completed 10 years school & High School'), ('University Degree', 'University Degree'), ('University Degree - Masters', 'University Degree - Masters'), ('Technical Degree', 'Technical Degree'), ('Others', 'Others')], default='Completed 10 years school', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee_profile',
            name='emergency_phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employee_profile',
            name='have_computer',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee_profile',
            name='license',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee_profile',
            name='parmanenet_address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employee_profile',
            name='present_address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employee_profile',
            name='working_hours',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]