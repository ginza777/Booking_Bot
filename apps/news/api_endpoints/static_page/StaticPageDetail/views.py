from rest_framework.generics import RetrieveAPIView

from apps.news.api_endpoints.static_page.StaticPageDetail.serializers import StaticPageDetailSerializer
from apps.news.models import StaticPage


class SlugRetrieveAPIView(RetrieveAPIView):
    lookup_field = "slug"
    lookup_url_kwarg = "slug"


class StaticPageDetailAPIView(SlugRetrieveAPIView):
    queryset = StaticPage.objects.all()
    serializer_class = StaticPageDetailSerializer


__all__ = ("StaticPageDetailAPIView",)
