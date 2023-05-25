from rest_framework.generics import ListAPIView

from apps.common.api_endpoints.country.CountryList.serializers import \
    CountrySerializer
from apps.common.models import Country


class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


__all__ = ("CountryListAPIView",)
