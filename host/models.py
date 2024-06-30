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
    country = CountryField(null=True)
    region = models.ForeignKey(Region, on_delete=models.RESTRICT, null=True)
    location = models.CharField(max_length=240, null=True)
    host_name = models.CharField(max_length=240, null=True)
    ipv4 = models.GenericIPAddressField(protocol='IPv4', null=True)
    ipv6 = models.GenericIPAddressField(protocol='IPv6', null=True)
    port = models.PositiveSmallIntegerField(null=True)  # PSIF may be limited to 32767 in some dbs
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.game_mode.game.name}[{self.game_mode.name}] "{self.name}"'

    class Meta:
        ordering = ('name', )
        unique_together = ('game_mode', 'name', )
