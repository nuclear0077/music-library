from django.urls import include, path
from rest_framework import routers
from .views import AlbumViewSet, ArtistViewSet, SongViewSet

router_v1 = routers.DefaultRouter()
router_v1.register('artists', ArtistViewSet, basename='artists')
router_v1.register('albums', AlbumViewSet, basename='albums')
router_v1.register('songs', SongViewSet, basename='songs')

urlpatterns = [
    path('', include(router_v1.urls), name='v1'),
]