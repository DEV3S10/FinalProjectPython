from django.contrib.auth import authenticate
from django.shortcuts import render
import datetime
import random
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ConfirmCode

# Create your views here.


class RegisterAPIView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User.objects.create_user(
            username=username,
            email="admin@gmail.com",
            password=password,
            is_active=False
        )
        code = str(random.randint(1000, 9999))
        valid_until = datetime.datetime.now() + datetime.timedelta(hours=24)
        ConfirmCode.objects.create(user=user, code=code, valid_until=valid_until)
        # send_code_to_phone(code, username)
        return Response(data={
            'massage': 'User created!!!'
        })


class ConfirmAPIView(APIView):

    def post(self, request):
        code = request.data['code']
        code_list = ConfirmCode.objects.filter(code=code)

        if code_list:
            user = code_list[0]
            user.is_active = True
            user.save()
            return Response(data={
                'massage': 'user activated!!!'
            })
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class LoginAPIView(APIView):
    def post(self, request):

        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user:
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)
            return Response(data={
                'token': token.key
            })
        else:
            return Response(data={
                'message': "User not found"
            }, status=status.HTTP_404_NOT_FOUND)

