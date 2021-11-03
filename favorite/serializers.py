from rest_framework import serializers
from .models import FavoriteNew, FavoriteLaw, FavoritePublication


class FavoriteNewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavoriteNew
        fields = '__all__'


class FavoriteLawsSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavoriteLaw
        fields = '__all__'


class FavoritePublicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavoritePublication
        fields = '__all__'
