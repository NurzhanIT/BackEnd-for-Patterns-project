from rest_framework import generics
from django.shortcuts import render

from users_api.models import User
from users_api.serializers import UsersSerializer


# Create your views here.


class UsersAPIList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
