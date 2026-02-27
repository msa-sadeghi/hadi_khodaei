from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Publisher, Contributor, Contact
from .forms import ContactForm, BookForm


def index(request):
    books = Book.objects.all()
    return render(request, "reviews/book_list.html", {"books": books})


def book_detail(request, id):
    details = Book.objects.get(id=id)
    return render(request, "reviews/book_details.html", {"details": details})


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            new_contact_object = Contact(name=name, email=email, message=message)
            new_contact_object.save()
            return render(request, "reviews/success.html")
    else:
        form = ContactForm()

    return render(request, "reviews/contact.html", {"form": form})


def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("reviews:create_book")
    else:
        form = BookForm()
    return render(request, "reviews/book_form.html", {"form": form})


def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("reviews:book_detail", id=book_id)
    else:
        form = BookForm(instance=book)
    return render(request, "reviews/edit_book.html", {"form": form})
