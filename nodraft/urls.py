from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path(
        settings.EMPTY_STRING, include(("gateway.urls", "gateway"), namespace="gateway")
    ),
    path("accounts/", include(("accounts.urls", "accounts"), namespace="accounts")),
    path("editor/", include(("editor.urls", "editor"), namespace="editor")),
    path("admin/", admin.site.urls),
    # Browser Reload
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
