from rest_framework.generics import ListAPIView

from apps.news.api_endpoints.news.NewsList.serializers import NewsSerializer
from apps.news.models import News


class NewsListAPIView(ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        return News.objects.all().order_by("-published_at")


__all__ = ("NewsListAPIView",)
