# Generated by Django 5.1.1 on 2024-10-07 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0002_alter_driver_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="driver",
            name="license_number",
            field=models.CharField(blank=True, max_length=250, null=True, unique=True),
        ),
    ]
