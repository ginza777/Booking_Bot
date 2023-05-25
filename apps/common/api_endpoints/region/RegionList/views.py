from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.common.api_endpoints.region.RegionList.serializers import \
    RegionSerializer
from apps.common.models import Region


class RegionListAPIView(GenericAPIView):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()

    def get(self, request, *args, **kwargs):
        country_pk = self.kwargs["pk"]
        news = self.get_queryset().filter(country_id=country_pk)
        serializer = self.serializer_class(news, many=True).data
        return Response(data=serializer, status=200)


__all__ = ("RegionListAPIView",)
