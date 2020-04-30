# Generated by Django 3.0.2 on 2020-04-30 22:58

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('images_collections', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='brain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=250)),
                ('gnb', models.BinaryField(null=True)),
                ('decisions_block', models.BinaryField(null=True)),
                ('internal_state', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('desired_state', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brain', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='am_net',
            fields=[
                ('brain_am_net', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='brain.brain')),
                ('index_ready_to_learn', models.IntegerField(default=0)),
                ('clack', models.BooleanField()),
                ('indexes_recognized', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='episodic_memory',
            fields=[
                ('brain_episodic_memory', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='brain.brain')),
                ('index_ready_to_learn', models.IntegerField(default=0)),
                ('clack', models.BooleanField()),
                ('indexes_recognized', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='rnb',
            fields=[
                ('brain_rnb', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='brain.brain')),
                ('index_ready_to_learn', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='snb_h',
            fields=[
                ('brain_h', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='brain.brain')),
                ('state', models.CharField(default='MISS?', max_length=280)),
                ('index_ready_to_learn', models.IntegerField()),
                ('last_learned_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='snb_s',
            fields=[
                ('brain_s', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='brain.brain')),
                ('state', models.CharField(default='MISS?', max_length=280)),
                ('index_ready_to_learn', models.IntegerField()),
                ('last_learned_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ss_rnb',
            fields=[
                ('brain_ss_rnb', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='brain.brain')),
                ('index_ready_to_learn', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='syllables_net',
            fields=[
                ('brain_syllables_net', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='brain.brain')),
                ('index_ready_to_learn', models.IntegerField(default=0)),
                ('clack', models.BooleanField()),
                ('indexes_recognized', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='words_net',
            fields=[
                ('brain_words_net', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='brain.brain')),
                ('index_ready_to_learn', models.IntegerField(default=0)),
                ('clack', models.BooleanField()),
                ('indexes_recognized', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SsRnbNeuron',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_knowledge', models.BooleanField()),
                ('hit', models.BooleanField()),
                ('knowledge', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('ss_rnb', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ss_rnb_neuron', to='brain.ss_rnb')),
            ],
        ),
        migrations.CreateModel(
            name='RnbNeuron',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_knowledge', models.BooleanField()),
                ('hit', models.BooleanField()),
                ('knowledge', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('rnb', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rnb_neuron', to='brain.rnb')),
            ],
        ),
        migrations.CreateModel(
            name='RbfNeuronSight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_knowledge', models.BooleanField()),
                ('radius', models.FloatField()),
                ('degraded', models.BooleanField()),
                ('knowledge', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('img', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image_related', to='images_collections.ImagesFromNeuron')),
                ('snb_sight', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rbf_neuron', to='brain.snb_s')),
            ],
        ),
        migrations.CreateModel(
            name='RbfNeuronHearing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_knowledge', models.BooleanField()),
                ('radius', models.FloatField()),
                ('degraded', models.BooleanField()),
                ('knowledge', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('snb_hearing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rbf_neuron', to='brain.snb_h')),
            ],
        ),
        migrations.CreateModel(
            name='IndexRecognizeSight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_recognize', models.IntegerField()),
                ('snb_sight', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='index_recognize', to='brain.snb_s')),
            ],
        ),
        migrations.CreateModel(
            name='IndexRecognizeHearing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_recognize', models.IntegerField()),
                ('snb_hearing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='index_recognize', to='brain.snb_h')),
            ],
        ),
        migrations.CreateModel(
            name='group_words_net',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_bip', models.IntegerField()),
                ('WordNetNeuron', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('words_net_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='words_net_group', to='brain.words_net')),
            ],
        ),
        migrations.CreateModel(
            name='group_syllables_net',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_bip', models.IntegerField()),
                ('SyllaNetNeuron', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('syllables_net_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='syllables_net_group', to='brain.syllables_net')),
            ],
        ),
        migrations.CreateModel(
            name='group_episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_bip', models.IntegerField()),
                ('episodicMemNeuron', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('episodic_memory_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='episode_group', to='brain.episodic_memory')),
            ],
        ),
        migrations.CreateModel(
            name='group_am_net',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_bip', models.IntegerField()),
                ('AmNetNeuron', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('am_net_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='am_net_group', to='brain.am_net')),
            ],
        ),
    ]
