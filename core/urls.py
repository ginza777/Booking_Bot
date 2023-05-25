from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .schema import swagger_urlpatterns

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path("bot/", include("apps.bot.urls")),
    path("api/v1/", include("apps.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),

    # rosetta
    path('rosetta/', include('rosetta.urls')),
]

urlpatterns += i18n_patterns(path("admin/", admin.site.urls), path("rosetta/", include("rosetta.urls")))

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
