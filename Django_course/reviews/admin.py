from django.contrib import admin
from .models import Book, Contributor, Publisher


admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Book)
