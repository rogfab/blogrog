from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

User = get_user_model()

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.CharField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Auteur")
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(blank=True, verbose_name="Contenu")
    thumbnail = models.ImageField(blank=True, upload_to='blog')

    class Meta:
        ordering = ['-created_on']
        verbose_name = "Article"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def author_or_default(self):
        return self.author.username if self.author else "L'auteur est inconnu"

    @property
    def thumbnail_url(self):
        if self.thumbnail and hasattr(self.thumbnail, 'url'):
            return self.thumbnail.url

    def get_absolute_url(self):
        return reverse('posts:home')

