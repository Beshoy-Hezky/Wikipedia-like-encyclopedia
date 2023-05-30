from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:topic>", views.content, name="content"),
    path("random", views.random_page, name="random")
]
