from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path(settings.EMPTY_STRING, include(("portal.urls", "portal"), namespace="portal")),
    path("accounts/", include(("accounts.urls", "accounts"), namespace="accounts")),
    path("document/", include(("document.urls", "document"), namespace="document")),
    path("admin/", admin.site.urls),
    # Browser Reload
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
