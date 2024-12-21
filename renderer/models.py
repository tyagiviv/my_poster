from django.db.models import CharField, Model
from django.db import models


# Create your models here.
class Poster(models.Model):
    objects = None
    url = CharField(max_length=256)

    def __str__(self):
        return self.url