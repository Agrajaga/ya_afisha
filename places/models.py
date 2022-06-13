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
    link = models.CharField(max_length=500)
    place = models.ForeignKey('Place', on_delete=models.CASCADE)
