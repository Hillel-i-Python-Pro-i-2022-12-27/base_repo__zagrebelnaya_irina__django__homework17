from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import about


urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("users/", include("apps.users.urls")),
    path("admin/", admin.site.urls),
    path("about/", about, name="about"),
    path("contactus/", include("apps.contact_us.urls")),
    path("", include("apps.users.urls_root")),
]
#
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
