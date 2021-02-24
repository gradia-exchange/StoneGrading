from django.db import models

from .grades import Inclusions


class Inclusion(models.Model):
    inclusion = models.CharField(choices=Inclusions.CHOICES, max_length=5, unique=True)

    def __str__(self):
        return self.inclusion
