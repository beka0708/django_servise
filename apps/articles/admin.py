from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "is_public", "created_at", "updated_at"]
    list_filter = ["is_public", "created_at", "author"]
    search_fields = ["title", "content", "author__email"]
    ordering = ["created_at"]
