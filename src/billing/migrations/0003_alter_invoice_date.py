# Generated by Django 5.0.6 on 2024-06-13 20:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_alter_invoice_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
