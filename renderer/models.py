from django.db.models import CharField, Model
from django.db import models


# Create your models here.
class Poster(models.Model):

    url = CharField(max_length=256, null = True)
    name = CharField(max_length=126, null=True)
    description = CharField(max_length=256, null=True)
    director_name = CharField(max_length=126, null=True)

    def __str__(self):
        if self.url is None:
            return 'vivek'
        else:
            return self.url


class Favorite(models.Model):

    poster_id = models.ForeignKey(Poster, on_delete=models.CASCADE, related_name="favorites")

    def __str__(self):
        return f"Favorite: {self.poster_id}"