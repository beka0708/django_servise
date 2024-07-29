from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "content",
            "is_public",
            "author",
            "created_at",
            "updated_at",
        ]
