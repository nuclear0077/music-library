from rest_framework import viewsets

from library.models import Artist, Album, Song
from .serializers import ArtistSerialiser, AlbumSerialiser, SongSerialiser


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerialiser


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerialiser


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerialiser
