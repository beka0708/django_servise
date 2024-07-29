from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import swagger

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/", include("apps.user.urls")),
    path("api/", include("apps.articles.urls")),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += swagger.urlpatterns
