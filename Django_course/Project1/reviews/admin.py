from django.contrib import admin
from .models import Book, Contributor, Publisher, BookContributor


admin.site.register(Publisher)
admin.site.register(Contributor)


class BookContributerInline(admin.StackedInline):
    model = BookContributor
    extra = 1


def mark_as_published(modeladmin, request, queryset):
    queryset.update(status="published")
    mark_as_published.short_descriptions = "Mark selected books as published"


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    actions = [mark_as_published]
    inlines = [BookContributerInline]
    list_display = ("title", "publisher", "publication_date", "isbn")
    list_filter = ("publisher",)
    search_fields = ("title", "isbn")
    date_hierarchy = "publication_date"
    fieldsets = (
        ("Book Information", {"fields": ("title", "isbn")}),
        (
            "Publication Details",
            {"fields": ("publisher", "publication_date", "status")},
        ),
    )
