# Generated by Django 2.2.7 on 2019-12-27 03:30

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brain', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rbfneuron',
            name='knowledge',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]