# Generated by Django 2.2.7 on 2019-12-30 19:47

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='brain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=250)),
                ('rnb', models.BinaryField(null=True)),
                ('am_net', models.BinaryField(null=True)),
                ('gnb', models.BinaryField(null=True)),
                ('syllables_net', models.BinaryField(null=True)),
                ('words_net', models.BinaryField(null=True)),
                ('ss_rnb', models.BinaryField(null=True)),
                ('episodic_memory', models.BinaryField(null=True)),
                ('decisions_block', models.BinaryField(null=True)),
                ('internal_state', models.BinaryField(null=True)),
                ('desired_state', models.BinaryField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brain', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='snb_h',
            fields=[
                ('brain_h', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='snb_h_json', serialize=False, to='brain.brain')),
                ('state', models.CharField(default='MISS?', max_length=280)),
                ('index_ready_to_learn', models.IntegerField()),
                ('last_learned_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='snb_s',
            fields=[
                ('brain_s', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='snb_s_json', serialize=False, to='brain.brain')),
                ('state', models.CharField(default='MISS?', max_length=280)),
                ('index_ready_to_learn', models.IntegerField()),
                ('last_learned_id', models.IntegerField()),
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
    ]
