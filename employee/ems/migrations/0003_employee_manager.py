# Generated by Django 2.2.4 on 2019-08-05 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0002_auto_20190805_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='manager',
            field=models.CharField(choices=[('employee', 'Employee'), ('manager', 'Manager')], default='employee', max_length=6),
        ),
    ]
