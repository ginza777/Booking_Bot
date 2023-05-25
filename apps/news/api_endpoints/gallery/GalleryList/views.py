from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.news.api_endpoints.gallery.GalleryList.serializers import \
    GallerySerializer
from apps.news.models import Gallery


class GalleryListAPIView(GenericAPIView):
    serializer_class = GallerySerializer
    queryset = Gallery.objects.all()

    def get(self, request, *args, **kwargs):
        folder_pk = self.kwargs["pk"]
        gallery = self.get_queryset().filter(folder_id=folder_pk)
        serializer = self.serializer_class(gallery, many=True, context={"request": request}).data
        return Response(data=serializer, status=200)


__all__ = ("GalleryListAPIView",)
