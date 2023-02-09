from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Author(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Имя Автора',
        unique=True
    )

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return f'Категория: {self.name}'


class Album(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название альбома',
        unique=True
    )

    author = models.ForeignKey(
        Author,
        related_name='author',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Автор Альбома')

    year = models.PositiveSmallIntegerField(
        verbose_name='Год выпуска альбома',
        validators=[MinValueValidator(1890), MaxValueValidator(2199)]
    )

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        constraints = [
            models.UniqueConstraint(
                fields=('name', 'author',),
                name='unique album'
            )]

    def __str__(self):
        return f'Альбом: {self.name}'


class Song(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название песни',
        unique=True
    )
    number = models.PositiveSmallIntegerField(
        verbose_name='Порядковый номер песни в альбоме'
    )
    album = models.ManyToManyField(Album, through='AlbumSong')

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'

    def __str__(self):
        return f'Песня: {self.name}'


class AlbumSong(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Альбом и песня'
        verbose_name_plural = 'Альбомы и песни'

    def __str__(self):
        return f'Альбом: {self.album} Песня: {self.song}'
