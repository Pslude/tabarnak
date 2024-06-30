"""
URL configuration for tabarnak project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import static
from django.views.generic.base import RedirectView

from django.conf import settings

urlpatterns = [

    # /admin/
    path('admin/', admin.site.urls),

    # /host/
    path('host/', include('host.urls')),

    # /favicon.ico
    path(
        'favicon.ico',
        RedirectView.as_view(
            url='/static/img/favicon.ico',
            permanent=True
        )
    ),

    # /robots.txt
    path(
        'robots.txt',
        lambda x: HttpResponse(
            f'User-agent: *\nDisallow: *\n',
            content_type='text/plain'
        ),
    ),

    # / (root)
    path(
        '',
        RedirectView.as_view(
            # url='https://tabarnak.io/',
            url='/host/',
            permanent=False
        )
    ),

]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.conf.urls.i18n import i18n_patterns
    from django.views import defaults as default_views
    from django.views.generic import TemplateView, RedirectView
    from django.http import Http404, HttpResponse

    # Serve static files, avoids needing to run "collectstatic" in dev
    urlpatterns += staticfiles_urlpatterns()

    # Debug toolbar
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

    # URLs for testing error pages in dev
    urlpatterns += i18n_patterns(
        path('400/', TemplateView.as_view(template_name='400.html')),
        path('403/', TemplateView.as_view(template_name='403.html')),
        path('404/', default_views.page_not_found, {'exception': Http404()}),
        path('500/', default_views.server_error),
    )
