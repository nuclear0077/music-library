from rest_framework import serializers

from library.models import Author, Song, Album, AlbumSong


class AuthorSerialiser(serializers.ModelSerializer):
    class Meta:
        fields = ('name',)
        model = Author


class AlbumSerialiser(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'author', 'year')
        model = Album


class SongSerialiser(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'number', 'album')
        model = Song
