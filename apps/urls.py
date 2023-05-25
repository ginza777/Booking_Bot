from django.urls import include, path

urlpatterns = [
    path("common/", include("apps.common.urls")),
    path("news/", include("apps.news.urls")),
    path("main/", include("apps.main.urls")),
    path("application/", include("apps.application.urls")),
]
