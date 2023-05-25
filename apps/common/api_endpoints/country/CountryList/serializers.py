from rest_framework.serializers import ModelSerializer

from apps.common.models import Country


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "name")
