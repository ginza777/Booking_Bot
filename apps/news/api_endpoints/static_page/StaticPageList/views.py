from rest_framework.generics import ListAPIView

from apps.news.api_endpoints.static_page.StaticPageList.serializers import StaticPageSerializer
from apps.news.models import StaticPage


class StaticPageListAPIView(ListAPIView):
    queryset = StaticPage.objects.all()
    serializer_class = StaticPageSerializer


__all__ = ("StaticPageListAPIView",)
