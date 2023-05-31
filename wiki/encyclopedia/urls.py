from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:topic>", views.content, name="content"),
    path("random/", views.random_page, name="random"),
    path("search/", views.search_box, name="search_box"),
    path("similarEntries/",views.search_box, name="similar_entries"),
    path("newPage/",views.new_page, name="new_page")
]
