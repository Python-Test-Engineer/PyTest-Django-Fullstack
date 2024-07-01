from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("homepage/", include("posts.urls"), name="homepage"),
    path("", include("posts.urls"), name="homepage"),
    path("admin/", admin.site.urls),
    path("posts/", include("posts.urls"), name="posts"),
    path("filemanager/", include("filemanager.urls")),
    path("accounts/", include("accounts.urls")),
    path("catalog/", include("catalog.urls")),
    path("ecommerce/", include("ecommerce.urls")),
    path("tracker/", include("tracker.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
