from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=150)
    description_short = models.CharField(max_length=500)
    description_long = models.TextField()
    coord_lng = models.FloatField()
    coord_lat = models.FloatField()

    def __str__(self) -> str:
        return self.title


class PlaceImage(models.Model):
    image = models.ImageField(blank=True, null=True)
    index = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
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
        ordering = ['index']
