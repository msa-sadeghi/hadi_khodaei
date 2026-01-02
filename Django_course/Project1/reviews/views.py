from django.shortcuts import render
from .models import Book, Publisher, Contributor


def index(request):
    books = Book.objects.all()
    return render(request, "reviews/book_list.html", {"books": books})


def book_detail(request, id):
    details = Book.objects.get(id=id)
    print(details)
    return render(request, "reviews/book_details.html", {"details": details})
