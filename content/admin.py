from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at', 'is_published', 'slug')
    list_filter = ('is_published', 'created_at', 'author')
    search_fields = ('title', 'content', 'slug')
    prepopulated_fields = {'slug': ('title',)}  # Позволяет автоматически генерировать слаг в админке
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
