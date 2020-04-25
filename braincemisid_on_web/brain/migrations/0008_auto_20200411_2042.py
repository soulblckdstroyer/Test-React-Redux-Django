# Generated by Django 3.0.2 on 2020-04-12 00:42

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brain', '0007_auto_20200408_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recognizedindexesepisodicmemory',
            name='episodic_memory_recognized_indexes',
        ),
        migrations.AddField(
            model_name='group',
            name='episodicMemNeuron',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='indexes_recognized',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='EpisodicMemNeuron',
        ),
        migrations.DeleteModel(
            name='RecognizedIndexesEpisodicMemory',
        ),
    ]
