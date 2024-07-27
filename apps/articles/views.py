from rest_framework import generics, permissions
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.exceptions import PermissionDenied


class PublicArticleListView(generics.ListAPIView):
    queryset = Article.objects.filter(is_public=True)
    serializer_class = ArticleSerializer
    permission_classes = [permissions.AllowAny]


class PrivateArticleListView(generics.ListAPIView):
    queryset = Article.objects.filter(is_public=False)
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]


class ArticleCreateView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.role != "AUTHOR":
            raise PermissionDenied("Только авторы могут создавать статьи.")
        serializer.save(author=self.request.user)


class ArticleUpdateView(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role == "AUTHOR" or self.request.user.is_staff:
            return Article.objects.filter(author=self.request.user)
        return Article.objects.none()


class ArticleDeleteView(generics.DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role == "AUTHOR" or self.request.user.is_staff:
            return Article.objects.filter(author=self.request.user)
        return Article.objects.none()
