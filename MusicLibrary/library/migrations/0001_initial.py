# Generated by Django 4.1.6 on 2023-02-10 10:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Album",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=256, unique=True, verbose_name="Название альбома"
                    ),
                ),
                ("slug", models.SlugField(unique=True)),
                (
                    "release_year",
                    models.PositiveSmallIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1890),
                            django.core.validators.MaxValueValidator(2199),
                        ],
                        verbose_name="Год выпуска альбома",
                    ),
                ),
            ],
            options={
                "verbose_name": "Альбом",
                "verbose_name_plural": "Альбомы",
            },
        ),
        migrations.CreateModel(
            name="AlbumSong",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "album",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="library.album"
                    ),
                ),
            ],
            options={
                "verbose_name": "Альбом и песня",
                "verbose_name_plural": "Альбомы и песни",
            },
        ),
        migrations.CreateModel(
            name="Artist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256, verbose_name="Имя артиста")),
                ("slug", models.SlugField(unique=True)),
            ],
            options={
                "verbose_name": "Артист",
                "verbose_name_plural": "Артисты",
            },
        ),
        migrations.CreateModel(
            name="Song",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=256, verbose_name="Название песни"),
                ),
                (
                    "track_number",
                    models.PositiveSmallIntegerField(
                        verbose_name="Порядковый номер песни в альбоме"
                    ),
                ),
                (
                    "album",
                    models.ManyToManyField(
                        through="library.AlbumSong", to="library.album"
                    ),
                ),
            ],
            options={
                "verbose_name": "Песня",
                "verbose_name_plural": "Песни",
            },
        ),
        migrations.AddField(
            model_name="albumsong",
            name="song",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="library.song"
            ),
        ),
        migrations.AddField(
            model_name="album",
            name="artist",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="artist",
                to="library.artist",
                verbose_name="Автор Альбома",
            ),
        ),
        migrations.AddConstraint(
            model_name="song",
            constraint=models.UniqueConstraint(
                fields=("name", "track_number"), name="unique name_track_number"
            ),
        ),
        migrations.AddConstraint(
            model_name="album",
            constraint=models.UniqueConstraint(
                fields=("name", "artist"), name="unique album"
            ),
        ),
    ]
