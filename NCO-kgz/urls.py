"""NCO_kgz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from account import views as account_view
from main import views as main_view
from favorite import views as favorite_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/register/', account_view.RegisterAPIView.as_view()),
    path('api/v1/confirm/', account_view.ConfirmAPIView.as_view()),
    path('api/v1/login/', account_view.LoginAPIView.as_view()),
    path('api/v1/news/', main_view.NewsListAPIView.as_view()),
    path('api/v1/news/<int:pk>', main_view.NewDetailUpdateDeleteAPIView.as_view()),
    path('api/v1/laws/', main_view.LawsListAPIView.as_view()),
    path('api/v1/laws/<int:pk>', main_view.LawDetailUpdateDeleteAPIView.as_view()),
    path('api/v1/publications/', main_view.PublicationsListAPIView.as_view()),
    path('api/v1/publications/<int:pk>', main_view.PublicationDetailUpdateDeleteAPIView.as_view()),
    path('api/v1/favoriteNews/', favorite_view.FavoriteNewsListAPIView.as_view()),
    path('api/v1/favoriteLaws/', favorite_view.FavoriteLawListAPIView.as_view()),
    path('api/v1/favoritePublications/', favorite_view.FavoritePublicationListAPIView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
