from rest_framework.generics import ListAPIView

from apps.main.api_endpoints.exhibitor.ExhibitorList.serializers import \
    ExhibitorSerializer
from apps.main.models import Exhibitor


class ExhibitorListAPIView(ListAPIView):
    serializer_class = ExhibitorSerializer

    def get_queryset(self):
        return Exhibitor.objects.all().order_by("order")


__all__ = ("ExhibitorListAPIView",)
