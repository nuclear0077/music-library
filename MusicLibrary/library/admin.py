from django.contrib import admin
from .models import Artist, Song, Album, AlbumSong


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'slug',
    )
    list_editable = ('name', 'slug',)
    search_fields = ('name', 'slug')
    list_filter = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'slug',
        'artist',
    )
    list_editable = ('name', 'slug',)
    search_fields = ('name', 'slug', 'artist')
    list_filter = ('name', 'artist')
    empty_value_display = '-пусто-'


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'track_number',
    )
    list_editable = ('name', 'track_number',)
    search_fields = ('name', 'album', 'track_number', )
    list_filter = ('name', 'album', 'track_number')
    empty_value_display = '-пусто-'


admin.site.register(AlbumSong)
