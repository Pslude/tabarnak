from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView, ListView, DetailView
from rest_framework import viewsets, permissions

from .models import Server, Region, Game, Studio
from .serializers import UserSerializer, GroupSerializer, ServerSerializer, RegionSerializer, StudioSerializer, \
    GameSerializer


class IndexView(ListView):
    template_name = 'host/index.html'
    model = Server
    queryset = Server.objects.filter(status='a')
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ServerProfileView(DetailView):
    template_name = 'host/server_profile.html'
    model = Server


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all().order_by('pk')
    serializer_class = ServerSerializer
    filterset_fields = [
        'game_mode__game__name',
        'game_mode__name',
        'status',
        'release__name',
    ]


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all().order_by('pk')
    serializer_class = RegionSerializer


class StudioViewSet(viewsets.ModelViewSet):
    queryset = Studio.objects.all().order_by('pk')
    serializer_class = StudioSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by('pk')
    serializer_class = GameSerializer
