# Generated by Django 5.0.6 on 2024-06-13 20:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 13, 20, 17, 34, 759683, tzinfo=datetime.timezone.utc)),
        ),
    ]