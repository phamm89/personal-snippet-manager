"""project_snippetmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings 
# Add static settings to serve up static files in development 
from django.conf.urls.static import static
# Core APP
from core import views as core_views
# Core_API APP
from rest_framework import routers
from core_api import views as core_api_views

router = routers.DefaultRouter()
router.register('customeruser', core_api_views.CustomUserViewSet)
router.register('snippet', core_api_views.SnippetViewSet)


urlpatterns = [
    path('', core_views.index, name='index'), 
    path('accounts/', include('registration.backends.simple.urls')),
    path('add_snippet/', core_views.add_snippet, name='add_snippet'),
    path('admin/core/snippet/<int:pk>/change/', core_views.SnippetUpdate.as_view(), name='edit_snippet'),
    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browsable API.
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns