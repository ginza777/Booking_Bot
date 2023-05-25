from rest_framework.generics import ListAPIView

from apps.main.api_endpoints.benifits_for_visitor.BenifitsForVisitorList.serializers import \
    BenifitsForVisitorSerializer
from apps.main.models import BenifitsForVisitor


class BenifitsForVisitorListAPIView(ListAPIView):
    serializer_class = BenifitsForVisitorSerializer

    def get_queryset(self):
        return BenifitsForVisitor.objects.all().order_by("order")


__all__ = ("BenifitsForVisitorListAPIView",)
