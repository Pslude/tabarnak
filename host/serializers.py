from django.contrib.auth.models import Group, User
from rest_framework import serializers

from host.models import Server, GameMode, Region, Studio, Game


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ServerSerializer(serializers.HyperlinkedModelSerializer):
    region = serializers.CharField(source='region.code')

    class Meta:
        model = Server
        fields = [
            'url',
            'id',
            'name',
            'location',
            'region',
            'country',
            'host_name',
            'port',
            'ipv4',
            'ipv6',
            'status',
            'last_ping',
            'last_ping_latency',
        ]
        extra_kwargs = {
            'url': {'view_name': 'host:server-detail'}
        }


class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region
        fields = [
            # 'url',
            'id',
            'name',
            'code',
            'centroid',
        ]
        # extra_kwargs = {
        #     'url': {'view_name': 'host:region-detail'}
        # }


class StudioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Studio
        fields = [
            # 'url',
            'id',
            'name',
        ]
        # extra_kwargs = {
        #     'url': {'view_name': 'host:studio-detail'}
        # }


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = [
            # 'url',
            'id',
            'name',
        ]
        # extra_kwargs = {
        #     'url': {'view_name': 'host:studio-detail'}
        # }
