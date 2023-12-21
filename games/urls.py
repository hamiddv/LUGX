from django.urls import path

from .views import *

app_name = "games"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("our-shop/", OurShopView.as_view(), name="our_shop"),
    path("game-detail/<int:id>/", GameDetailView.as_view(), name="game-detail"),
]
