from rest_framework import serializers
from django.core.exceptions import ValidationError
from library.models import Artist, Song, Album


class ArtistSerialiser(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Artist


class AlbumSerialiser(serializers.ModelSerializer):
    artist = serializers.SlugRelatedField(
        queryset=Artist.objects.all(),
        slug_field='slug')

    class Meta:
        fields = ('name', 'slug', 'artist', 'release_year',)
        model = Album


class SongSerialiser(serializers.ModelSerializer):
    album = serializers.SlugRelatedField(
        queryset=Album.objects.all(),
        slug_field='slug',
        many=True)

    class Meta:
        fields = ('name', 'track_number', 'album')
        model = Song

    def validate(self, data):
        print(data.get('album'))
        song = Song.objects.filter(
            name=data.get('name'),
            track_number=data.get('track_number')
        )
        if song.exists():
            raise ValidationError('track_number должен быть другой')
        return data
