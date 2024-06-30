from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView
from rest_framework import viewsets, permissions

from .serializers import UserSerializer, GroupSerializer


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