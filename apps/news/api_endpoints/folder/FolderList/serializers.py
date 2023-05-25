from rest_framework.serializers import ModelSerializer

from apps.news.models import Folder


class FolderSerializer(ModelSerializer):
    class Meta:
        model = Folder
        fields = ("id", "name", "image")
