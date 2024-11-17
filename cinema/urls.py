from django.urls import path, include
from rest_framework import routers


from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
)

app_name = "cinema"

router = routers.DefaultRouter()


router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinemahalls", CinemaHallViewSet)
router.register("movies", MovieViewSet)
router.register("moviesessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
