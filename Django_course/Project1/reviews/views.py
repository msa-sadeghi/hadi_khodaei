from django.shortcuts import render
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
            # TODO implement action to add this record into database
            new_contact_object = Contact(name=name, email=email, message=message)
            new_contact_object.save()
            return render(request, "reviews/success.html")
    else:
        form = ContactForm()

    return render(request, "reviews/contact.html", {"form": form})


def create_book(request):
    form = BookForm()
    return render(request, "reviews/book_form.html", {"form": form})


