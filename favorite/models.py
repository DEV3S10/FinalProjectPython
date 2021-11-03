from django.contrib.auth.models import User
from django.db import models
from main.models import New, Law, Publication
# Create your models here.


class FavoriteNew(models.Model):
    news = models.ForeignKey(New, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class FavoriteLaw(models.Model):
    law = models.ForeignKey(Law, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class FavoritePublication(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
