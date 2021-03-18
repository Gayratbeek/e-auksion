"""Auksion site URL Configuration
"""
from django.urls import include, path
from rest_framework import routers
from lots import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from lots.feeds import RssFeed
from .yasg import urlpatterns as doc_urls

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('rss/feed', RssFeed(), name='rss-feed'),
    path('admin/', admin.site.urls),
    path('api/v1/base-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/lots/', include('lots.urls', namespace='lots-api')),
    path('api/v1/accounts/', include('account.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    # path('', include(router.urls)),
]

urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)