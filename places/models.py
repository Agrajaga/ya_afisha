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
    index = models.PositiveSmallIntegerField(unique=True, null=True)
    place = models.ForeignKey('Place', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.index} {self.place.title}'
