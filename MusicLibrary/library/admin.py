from django.contrib import admin
from .models import Author, Song, Album, AlbumSong
# Register your models here.

admin.site.register(Author)
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(AlbumSong)