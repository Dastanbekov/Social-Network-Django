from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
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
    slug = models.SlugField(verbose_name='slug', blank=False,null=False,unique=True,max_length=255,default='none')

    def save(self, *args, **kwargs):
        if not self.slug:  # Генерация слага, если он не установлен
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['-created_at']
