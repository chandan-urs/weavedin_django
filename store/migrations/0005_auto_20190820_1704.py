# Generated by Django 2.2.4 on 2019-08-20 11:34

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20190820_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='properties',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), null=True, size=None),
        ),
    ]
