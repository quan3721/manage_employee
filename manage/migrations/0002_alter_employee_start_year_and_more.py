# Generated by Django 4.2.7 on 2023-11-23 16:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("manage", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="start_year",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="employee",
            name="total_attend",
            field=models.IntegerField(),
        ),
    ]