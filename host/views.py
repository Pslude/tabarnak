from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView
from rest_framework import viewsets, permissions

from .models import Server, Region, Game, Studio
from .serializers import UserSerializer, GroupSerializer, ServerSerializer, RegionSerializer, StudioSerializer, \
    GameSerializer


class IndexView(TemplateView):
    template_name = 'host/index.html'


class HostDetailView(TemplateView):
    template_name = 'host/host_detail.html'


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ServerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows servers to be viewed or edited.
    """
    queryset = Server.objects.all().order_by('pk')
    serializer_class = ServerSerializer
    filterset_fields = [
        'game_mode__game__name',
        'game_mode__name',
        'status',
        'release__name',
    ]


class RegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows regions to be viewed.
    """
    queryset = Region.objects.all().order_by('pk')
    serializer_class = RegionSerializer


class StudioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows regions to be viewed.
    """
    queryset = Studio.objects.all().order_by('pk')
    serializer_class = StudioSerializer


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows regions to be viewed.
    """
    queryset = Game.objects.all().order_by('pk')
    serializer_class = GameSerializer
