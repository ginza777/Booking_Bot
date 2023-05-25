from rest_framework.generics import ListAPIView

from apps.main.api_endpoints.product_group.ProductGroupList.serializers import \
    ProductGroupSerializer
from apps.main.models import ProductGroup


class ProductGroupListAPIView(ListAPIView):
    serializer_class = ProductGroupSerializer

    def get_queryset(self):
        return ProductGroup.objects.all().order_by("order")


__all__ = ("ProductGroupListAPIView",)
