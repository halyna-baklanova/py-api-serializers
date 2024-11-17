from rest_framework import viewsets

from cinema.models import Genre
from cinema.serializers import (
    GenreSerializer,
    ActorSerializers,
    CinemaHallSerializer,
    MovieSerializer,
    MovieSessionSerializer,
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = ActorSerializers


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = MovieSessionSerializer
