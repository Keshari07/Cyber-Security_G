# Generated by Django 4.2.8 on 2024-01-09 14:31
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ingestors_manager", "0016_1_change_primary_key"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ingestorreport",
            name="config",
            field=models.CharField(max_length=100, null=False, blank=False),
        ),
    ]
