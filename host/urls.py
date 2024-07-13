from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views

app_name = 'host'

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
router.register(r'servers', views.ServerViewSet)
router.register(r'regions', views.RegionViewSet)
router.register(r'studios', views.StudioViewSet)
router.register(r'games', views.GameViewSet)

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('server/<int:pk>/', views.ServerProfileView.as_view(), name='server-profile'),

    # REST framework API
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', obtain_auth_token),
]
