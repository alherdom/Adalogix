# Generated by Django 5.0.3 on 2024-05-05 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_employee_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='route',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
