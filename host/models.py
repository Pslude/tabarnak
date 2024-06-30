from django.conf import settings
from django.contrib.gis.db.models import PointField
from django.db import models
from django_countries.fields import CountryField


class Studio(models.Model):
    name = models.CharField(max_length=240, unique=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)
    country = CountryField(null=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Game(models.Model):
    name = models.CharField(max_length=240, unique=True)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class GameMode(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=240)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.game.name}: {self.name}'

    class Meta:
        ordering = ('name', )
        unique_together = ('game', 'name', )


class Release(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=240)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.game.name} v. {self.name}'

    class Meta:
        ordering = ('-name', )
        unique_together = ('game', 'name', )


class Region(models.Model):
    name = models.CharField(max_length=240, unique=True)
    code = models.CharField(max_length=3, unique=True)
    centroid = PointField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )

class Server(models.Model):
    name = models.CharField(max_length=240)
    game_mode = models.ForeignKey(GameMode, on_delete=models.CASCADE)
    release = models.ForeignKey(Release, on_delete=models.CASCADE)
    country = CountryField()
    region = models.ForeignKey(Region, on_delete=models.RESTRICT)
    location = models.CharField(max_length=240)
    host_name = models.CharField(max_length=240)
    port = models.SmallIntegerField()
    ipv4 = models.GenericIPAddressField(protocol='IPv4', null=True)
    ipv6 = models.GenericIPAddressField(protocol='IPv6', null=True)
    max_players = models.PositiveSmallIntegerField(default=1)
    player_count = models.PositiveSmallIntegerField(default=0)
    max_spectators = models.PositiveSmallIntegerField(default=0)
    spectator_count = models.PositiveSmallIntegerField(default=0)
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    last_ping = models.DateTimeField(null=True, blank=True)
    last_ping_latency = models.PositiveSmallIntegerField(null=True, blank=True)
    STATUS_CHOICES = (
        ('n', 'New'),
        ('a', 'Active'),
        ('o', 'Offline'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='n')

    def __str__(self):
        return f'{self.game_mode.game.name}[{self.game_mode.name}] "{self.name}"'

    class Meta:
        ordering = ('name', )
        unique_together = ('game_mode', 'name', )
