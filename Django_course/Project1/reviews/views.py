from django.shortcuts import render
from .models import Book, Publisher, Contributor
from .forms import ContactForm, BookForm


def index(request):
    books = Book.objects.all()
    return render(request, "reviews/book_list.html", {"books": books})


def book_detail(request, id):
    details = Book.objects.get(id=id)
    print(details)
    return render(request, "reviews/book_details.html", {"details": details})


def contact_view(request):
    form = ContactForm()
    return render(request, "reviews/contact.html", {"form": form})


def create_book(request):
    form = BookForm()
    return render(request, "reviews/book_form.html", {"form": form})
