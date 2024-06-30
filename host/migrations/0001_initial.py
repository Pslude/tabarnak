# Generated by Django 5.0.6 on 2024-06-30 22:02

import django.contrib.gis.db.models.fields
import django.db.models.deletion
import django_countries.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240, unique=True)),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240, unique=True)),
                ('code', models.CharField(max_length=3, unique=True)),
                ('centroid', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='GameMode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
                ('created', models.DateField(auto_now_add=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='host.game')),
            ],
            options={
                'ordering': ('name',),
                'unique_together': {('game', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
                ('created', models.DateField(auto_now_add=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='host.game')),
            ],
            options={
                'ordering': ('-name',),
                'unique_together': {('game', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240, unique=True)),
                ('country', django_countries.fields.CountryField(max_length=2, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='game',
            name='studio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='host.studio'),
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('location', models.CharField(max_length=240)),
                ('host_name', models.CharField(max_length=240)),
                ('port', models.SmallIntegerField()),
                ('ipv4', models.GenericIPAddressField(null=True, protocol='IPv4')),
                ('ipv6', models.GenericIPAddressField(null=True, protocol='IPv6')),
                ('max_players', models.PositiveSmallIntegerField(default=1)),
                ('player_count', models.PositiveSmallIntegerField(default=0)),
                ('max_spectators', models.PositiveSmallIntegerField(default=0)),
                ('spectator_count', models.PositiveSmallIntegerField(default=0)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('last_ping', models.DateTimeField(null=True)),
                ('last_ping_latency', models.PositiveSmallIntegerField(null=True)),
                ('status', models.CharField(choices=[('n', 'New'), ('a', 'Active'), ('o', 'Offline')], default='n', max_length=1)),
                ('game_mode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='host.gamemode')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='host.region')),
                ('release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='host.release')),
            ],
            options={
                'ordering': ('name',),
                'unique_together': {('game_mode', 'name')},
            },
        ),
    ]
