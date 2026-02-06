from django.urls import path
from . import views

app_name = "reviews"
urlpatterns = [
    path("", views.index, name="index"),
    path("add_book/", views.create_book, name="create_book"),
    path("contact/", views.contact_view, name="contact_view"),
    path("book/<int:id>/", views.book_detail, name="book_detail"),
]
