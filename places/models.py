from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description_short = models.TextField(
        blank=True, verbose_name='Краткое описание')
    description_long = HTMLField(
        blank=True, verbose_name='Полное описание')
    coord_lng = models.FloatField(verbose_name='Долгота')
    coord_lat = models.FloatField(verbose_name='Широта')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'
        unique_together = [['title', 'coord_lng', 'coord_lat']]


class PlaceImage(models.Model):
    image = models.ImageField(verbose_name='Картинка')
    index = models.PositiveSmallIntegerField(
        default=0,
        db_index=True
    )
    place = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        related_name='imgs')

    def __str__(self) -> str:
        return f'{self.index} {self.place.title}'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['index']
