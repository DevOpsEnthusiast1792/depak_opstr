# Generated by Django 2.2.4 on 2019-08-05 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0009_employee_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(blank=True, choices=[('manager', 'Manager')], max_length=20, null=True),
        ),
    ]
