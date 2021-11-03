from django.contrib import admin
from .models import New, ImageNews, Publication, Law

# Register your models here.

admin.site.register(New)
admin.site.register(ImageNews)
admin.site.register(Law)
admin.site.register(Publication)
