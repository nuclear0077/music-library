from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Artist(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Имя артиста'
    )
    slug = models.SlugField(
        unique=True,
    )

    class Meta:
        verbose_name = 'Артист'
        verbose_name_plural = 'Артисты'

    def __str__(self):
        return f'Артист: {self.name}'


class Album(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название альбома',
        unique=True
    )
    slug = models.SlugField(
        unique=True,
    )
    artist = models.ForeignKey(
        Artist,
        related_name='artist',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Автор Альбома')

    release_year = models.PositiveSmallIntegerField(
        verbose_name='Год выпуска альбома',
        validators=[MinValueValidator(1890), MaxValueValidator(2199)]
    )

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        constraints = [
            models.UniqueConstraint(
                fields=('name', 'artist',),
                name='unique album'
            )]

    def __str__(self):
        return f'Альбом: {self.name}'


class Song(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название песни',
    )
    track_number = models.PositiveSmallIntegerField(
        verbose_name='Порядковый номер песни в альбоме'
    )
    album = models.ManyToManyField(Album, through='AlbumSong')

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'
        constraints = [
            models.UniqueConstraint(
                fields=('name', 'track_number',),
                name='unique name_track_number'
            )]

    def __str__(self):
        return f'Песня: {self.name}'


class AlbumSong(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Альбом и песня'
        verbose_name_plural = 'Альбомы и песни'

    def __str__(self):
        return f'{self.album} {self.song}'
