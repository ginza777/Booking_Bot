from rest_framework.serializers import ModelSerializer

from apps.main.models import AboutUs


class AboutUsSerializer(ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ("id", "text")
