from rest_framework.serializers import ModelSerializer

from apps.main.models import Partner


class PartnerSerializer(ModelSerializer):
    class Meta:
        model = Partner
        fields = ("id", "image", "link")
