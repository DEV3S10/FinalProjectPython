from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import New, Law, Publication
from favorite.models import FavoriteLaw, FavoritePublication, FavoriteNew


class NewsListSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = New
        fields = 'id image title short_description publication_date is_favorite'.split()

    def get_is_favorite(self, news):
        request = self.context['request']
        return bool(request.user.is_authenticated and FavoriteNew.objects.filter(news=news, user=request.user))


class NewsValidateSerializer(serializers.Serializer):
    pass


class NewFullListSerializer(serializers.ModelSerializer):

    class Meta:
        model = New
        fields = '__all__'


class LawListSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = Law
        fields = 'id title short_description'.split()

    def get_is_favorite(self, law):
        request = self.context['request']
        return bool(request.user.is_authenticated and FavoriteLaw.objects.filter(law=law, user=request.user))


class LawFullListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Law
        fields = '__all__'


class PublicationListSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = Publication
        fields = '__all__'

    def get_is_favorite(self, publication):
        request = self.context['request']
        return bool(request.user.is_authenticated and FavoritePublication.objects.filter(publication=publication, user=request.user))


class NewValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    short_description = serializers.CharField(min_length=1, max_length=100)
    full_description = serializers.CharField(min_length=1, max_length=150)
    is_main = serializers.BooleanField(default=False)
    link = serializers.CharField()

    def validate_title(self, title):
        news = New.objects.filter(title=title)
        if news.count() > 0:
            raise ValidationError("news with the same title already exists")
        return title

    def validate_link(self, link):
        array = link.split()
        print(len(array))
        if (len(array) > 1):
            raise ValidationError("Введите рабочую ссылку!")
        return link


class LawValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=100)
    short_description = serializers.CharField(min_length=1, max_length=50)
    full_description = serializers.CharField(min_length=1, max_length=100)
    type = serializers.IntegerField()

    def validate_title(self, title):
        laws = Law.objects.filter(title=title)
        if laws.count() > 0:
            raise ValidationError("law with the same title already exists")
        return title

    def validate_type(self, type):
        if type < 1 or type > 3:
            raise ValidationError("Вы можете выбрать только от 1 до 3")
        return type


class PublicationValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=100)
    short_description = serializers.CharField(min_length=1, max_length=50)
    full_description = serializers.CharField(min_length=1, max_length=100)
    type = serializers.IntegerField()

    def validate_title(self, title):
        publication = Publication.objects.filter(title=title)
        if publication.count() > 0:
            raise ValidationError("publication with the same title already exists")
        return title

    def validate_type(self, type):
        if type < 1 or type > 2:
            raise ValidationError("Вы можете выбрать только от 1 до 2")
        return type
