from django.db import models

from catalog.models import Work

# Create your models here.

class Ebook(Work):
    pages_number = models.PositiveSmallIntegerField()
    genres = models.ManyToManyField('catalog.Genre')
    authors = models.ManyToManyField('catalog.Author')

    def __str__(self):
        return self.title