from django.urls import include, path
from rest_framework import routers
from .views import AlbumViewSet, AuthorViewSet, SongViewSet

router_v1 = routers.DefaultRouter()
router_v1.register('authors', AlbumViewSet, basename='authors')
router_v1.register('albums', AuthorViewSet, basename='albums')
router_v1.register('songs', SongViewSet, basename='songs')

urlpatterns = [
    path('', include(router_v1.urls), name='v1'),
]