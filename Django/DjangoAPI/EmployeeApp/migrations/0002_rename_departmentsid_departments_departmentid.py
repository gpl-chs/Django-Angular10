# Generated by Django 4.2.7 on 2023-11-10 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departments',
            old_name='DepartmentsId',
            new_name='DepartmentId',
        ),
    ]
