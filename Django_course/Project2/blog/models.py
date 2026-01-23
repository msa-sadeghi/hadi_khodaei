from django.db import models
from django.utils import timezone

class Article(models.Model):
    STATUS_CHOICES = [
        ('draft', 'draft'),
        ('published', 'published')
    ]
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey('Category',
                                  on_delete=models.CASCADE,
                                  related_name='articles'
                                    )
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,default='draft')

    def __str__(self):
        return self.title
    
    def publish(self):
        self.status = 'published'
        self.published_at = timezone.now()
        self.save()

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="category"
        verbose_name_plural = "categories"