# Generated by Django 5.0.6 on 2024-06-03 14:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IdentityAPP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 3, 14, 18, 17, 689120, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='phonenumber',
            field=models.CharField(max_length=10, null=True),
        ),
    ]