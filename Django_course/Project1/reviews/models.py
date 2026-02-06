from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=50, help_text="The name of the publisher")
    website = models.URLField(help_text="The publisher's webite")
    email = models.EmailField(help_text="The publisher's email address")

    def __str__(self):
        return self.name


class Contributor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.first_name


class Book(models.Model):
    PUBLICATION_STATUS = (("published", "published"), ("unpublished", "unpublished"))
    title = models.CharField(max_length=70)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=20)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField(Contributor, through="BookContributor")
    status = models.CharField(
        max_length=100, choices=PUBLICATION_STATUS, default="unpublished"
    )

    def __str__(self):
        return self.title


class BookContributor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=30, help_text="Role of the contributor (e.g. Auther, Editor)"
    )
