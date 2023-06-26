from .models import *
from rest_framework import serializers


class MovieDataBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieDataBase
        fields = '__all__'
