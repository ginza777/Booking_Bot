from rest_framework.serializers import ModelSerializer

from apps.main.models import ProductGroup


class ProductGroupSerializer(ModelSerializer):
    class Meta:
        model = ProductGroup
        fields = ("id", "title", "description", "icon")
