# Generated by Django 5.0.1 on 2024-01-30 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_alter_patientmodel_age_alter_patientmodel_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientmodel',
            name='status',
            field=models.CharField(default='pending', max_length=50),
        ),
    ]
