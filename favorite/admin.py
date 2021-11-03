from django.contrib import admin
from .models import FavoriteNew, FavoriteLaw, FavoritePublication
# Register your models here.

admin.site.register(FavoriteNew)
admin.site.register(FavoriteLaw)
admin.site.register(FavoritePublication)
