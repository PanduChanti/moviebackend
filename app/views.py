from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

# Create your views here.


class MovieList(ListAPIView):
    queryset = MovieDataBase.objects.all()
    serializer_class = MovieDataBaseSerializer


class MovieCreate(CreateAPIView):
    queryset = MovieDataBase.objects.all()
    serializer_class = MovieDataBaseSerializer


class MovieRev(RetrieveAPIView):
    queryset = MovieDataBase.objects.all()
    serializer_class = MovieDataBaseSerializer


class MovieUpdate(UpdateAPIView):
    queryset = MovieDataBase.objects.all()
    serializer_class = MovieDataBaseSerializer


class MovieDelete(DestroyAPIView):
    queryset = MovieDataBase.objects.all()
    serializer_class = MovieDataBaseSerializer
