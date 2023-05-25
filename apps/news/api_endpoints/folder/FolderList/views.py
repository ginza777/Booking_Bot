from rest_framework.generics import ListAPIView

from apps.news.api_endpoints.folder.FolderList.serializers import \
    FolderSerializer
from apps.news.models import Folder


class FolderListAPIView(ListAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer


__all__ = ("FolderListAPIView",)
