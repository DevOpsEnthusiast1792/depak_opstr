# Generated by Django 2.2.4 on 2019-08-05 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0007_employee_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='status',
        ),
    ]
