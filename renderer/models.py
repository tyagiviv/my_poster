from django.db.models import CharField, Model


# Create your models here.
class Poster(Model):
    url = CharField(max_length=256)
