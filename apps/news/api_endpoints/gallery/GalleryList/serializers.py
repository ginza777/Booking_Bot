from rest_framework.serializers import ModelSerializer

from apps.news.models import Gallery


class GallerySerializer(ModelSerializer):
    class Meta:
        model = Gallery
        fields = ("id", "name", "image")
