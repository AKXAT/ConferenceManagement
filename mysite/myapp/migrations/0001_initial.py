# Generated by Django 3.2.4 on 2021-10-02 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConferenceModel',
            fields=[
                ('conference_title', models.TextField(primary_key=True, serialize=False)),
                ('conference_description', models.CharField(max_length=1000)),
                ('conference_start_date', models.DateField()),
                ('conference_end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TalkModel',
            fields=[
                ('talk_title', models.TextField(primary_key=True, serialize=False)),
                ('talk_description', models.CharField(max_length=100)),
                ('talk_duration', models.DecimalField(decimal_places=1, max_digits=2)),
                ('talk_time', models.DateTimeField()),
                ('talk_conference_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.conferencemodel')),
            ],
        ),
        migrations.CreateModel(
            name='SpeakerModal',
            fields=[
                ('speaker_username', models.CharField(max_length=25)),
                ('speaker_email', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('speaker_talk_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.talkmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantModel',
            fields=[
                ('participant_username', models.CharField(max_length=25)),
                ('participant_email', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('participant_talk_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.talkmodel')),
            ],
        ),
    ]
