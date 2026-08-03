from django.db import models

from catalog.models import Work

# Create your models here.

class Movie(Work):
    duration = models.PositiveSmallIntegerField()
    subtitle = models.URLField(blank=True)
    origin = models.CharField(max_length=255)
    genres = models.ManyToManyField('catalog.Genre')
    authors = models.ManyToManyField('catalog.Author')

    def __str__(self):
        return self.title