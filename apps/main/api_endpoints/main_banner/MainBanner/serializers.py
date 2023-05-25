from rest_framework.serializers import ModelSerializer

from apps.main.models import MainBanner


class MainBannerSerializer(ModelSerializer):
    class Meta:
        model = MainBanner
        fields = ("id", "title", "sub_title", "banner", "arranged_date")
