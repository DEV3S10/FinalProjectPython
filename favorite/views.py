from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import FavoriteLaw, FavoriteNew, FavoritePublication
from .serializers import FavoriteLawsSerializer, FavoriteNewsSerializer, FavoritePublicationSerializer
# Create your views here.


class FavoriteLawListAPIView(APIView):
    def get(self, request):
        law = FavoriteLaw.objects.all()
        data = FavoriteLawsSerializer(law, many = True, context={"request": request}).data
        return Response(data=data)


class FavoriteNewsListAPIView(APIView):
    def get(self, request):
        law = FavoriteNew.objects.all()
        data = FavoriteNewsSerializer(law, many = True, context={"request": request}).data
        return Response(data=data)


class FavoritePublicationListAPIView(APIView):

    def get(self, request):
        law = FavoritePublication.objects.all()
        data = FavoritePublicationSerializer(law, many = True, context={"request": request}).data
        return Response(data=data)
