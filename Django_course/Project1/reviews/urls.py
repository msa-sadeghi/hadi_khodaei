from django.urls import path
from . import views

app_name = "reviews"
urlpatterns = [
    path("", views.index, name="index"),
    path("book/<int:id>/", views.book_detail, name="book_detail"),
]
