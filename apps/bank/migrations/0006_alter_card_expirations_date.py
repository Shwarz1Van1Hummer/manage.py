# Generated by Django 4.1.7 on 2023-03-11 16:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bank", "0005_alter_card_expirations_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="card",
            name="expirations_date",
            field=models.DateField(
                default=datetime.datetime(2026, 3, 10, 22, 56, 34, 767643),
                verbose_name="Срок годности",
            ),
        ),
    ]
