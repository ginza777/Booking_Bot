from rest_framework.generics import ListAPIView

from apps.main.api_endpoints.partner.PartnerList.serializers import \
    PartnerSerializer
from apps.main.models import Partner


class PartnerListAPIView(ListAPIView):
    serializer_class = PartnerSerializer

    def get_queryset(self):
        return Partner.objects.all().order_by("order")


__all__ = ("PartnerListAPIView",)
