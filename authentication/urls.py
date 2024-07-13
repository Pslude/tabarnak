from django.conf.urls.i18n import i18n_patterns
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from . import views

app_name = 'authentication'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('join/', views.JoinView.as_view(), name='join'),
    path('join/done/', views.JoinDoneView.as_view(), name='join_done'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logged_out/', views.LoggedOutView.as_view(), name='logged_out'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='authentication/password_change_form.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='authentication/password_change_done.html'), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='authentication/password_reset_form.html', success_url = reverse_lazy('authentication:password_reset_done')), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='authentication/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='authentication/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='authentication/password_reset_complete.html'), name='password_reset_complete'),
]
