from django.urls import path
from .views import (
    PublicArticleListView,
    PrivateArticleListView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
)

urlpatterns = [
    path("public/", PublicArticleListView.as_view(), name="public_articles"),
    path("private/", PrivateArticleListView.as_view(), name="private_articles"),
    path("create/", ArticleCreateView.as_view(), name="article_create"),
    path("update/<int:pk>/", ArticleUpdateView.as_view(), name="article_update"),
    path("delete/<int:pk>/", ArticleDeleteView.as_view(), name="article_delete"),
]
