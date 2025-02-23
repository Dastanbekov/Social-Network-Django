from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from unidecode import unidecode
# Create your models here.  

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Контент")
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="posts",
        verbose_name="Автор"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    slug = models.SlugField(verbose_name='slug',
                             blank=True,
                             unique=True,
                             max_length=255)

    def generate_unique_slug(self):
        base_slug = slugify(unidecode(self.title))
        if not base_slug: 
            base_slug = "post"  
        slug = base_slug
        num = 1
        while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{num}"
            num += 1
        return slug

    def save(self, *args, **kwargs):
        # Generate slug only if it’s not set or is blank
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['-created_at']