from rest_framework.generics import RetrieveAPIView

from apps.news.api_endpoints.news.NewsDetail.serializers import \
    NewsDetailSerializer
from apps.news.models import News


class SlugRetrieveAPIView(RetrieveAPIView):
    lookup_field = "slug"
    lookup_url_kwarg = "slug"


class NewsDetailAPIView(SlugRetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer


__all__ = ("NewsDetailAPIView",)
