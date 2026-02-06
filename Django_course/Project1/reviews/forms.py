from django import forms
from .models import Book


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField()


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("title", "publisher")
