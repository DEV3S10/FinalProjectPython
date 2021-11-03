import datetime
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import New, Law, Publication
from main.serializers import NewsListSerializer, NewValidateSerializer, PublicationListSerializer, LawListSerializer


# Create your views here.


class NewsListAPIView(APIView):
    def get(self, request):
        news = New.objects.all()
        data = NewsListSerializer(news, many=True, context={'request': request}).data
        return Response(data=data)

    def post(self, request):
        form = request.data
        serializer = NewValidateSerializer(data=form)
        if not serializer.is_valid():
            return Response(
                data={'message': 'error',
                      'errors': serializer.errors},
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
        title = form['title']
        short_description = form['short_description']
        full_description = form['full_description']
        link = form['link']
        New.objects.create(title=title,
                            short_description=short_description,
                            full_description=full_description,
                            publication_date=datetime.datetime.now(),
                            link=link)
        return Response(data={"Message": "News added"})


class LawsListAPIView(APIView):

    def get(self, request):
        law = Law.objects.all()
        data = NewsListSerializer(law, many=True, context={'request': request}).data
        return Response(data=data)

    def post(self, request):
        form = request.data
        serializer = NewValidateSerializer(data=form)
        if not serializer.is_valid():
            return Response(
                data={'message': 'error',
                      'errors': serializer.errors},
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
        title = form['title']
        short_description = form['short_description']
        full_description = form['full_description']
        link = form['link']
        New.objects.create(title=title,
                            short_description=short_description,
                            full_description=full_description,
                            publication_date=datetime.datetime.now(),
                            link=link)
        return Response(data={"Message": "News added"})


class PublicationsListAPIView(APIView):

    def get(self, request):
        publication = Publication.objects.all()
        data = NewsListSerializer(publication, many=True, context={'request': request}).data
        return Response(data=data)

    def post(self, request):
        form = request.data
        serializer = NewValidateSerializer(data=form)
        if not serializer.is_valid():
            return Response(
                data={'message': 'error',
                      'errors': serializer.errors},
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
        title = form['title']
        short_description = form['short_description']
        full_description = form['full_description']
        link = form['link']
        New.objects.create(title=title,
                            short_description=short_description,
                            full_description=full_description,
                            publication_date=datetime.datetime.now(),
                            link=link)
        return Response(data={"Message": "News added"})


class NewDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated)
    queryset = New.objects.all()
    serializer_class = NewsListSerializer


class LawDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Law.objects.all()
    serializer_class = LawListSerializer


class PublicationDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationListSerializer
