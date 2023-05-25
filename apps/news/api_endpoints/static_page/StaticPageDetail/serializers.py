from rest_framework.serializers import ModelSerializer

from apps.news.models import StaticPage


class StaticPageDetailSerializer(ModelSerializer):
    class Meta:
        model = StaticPage
        fields = (
            "id",
            "title",
            "body",
        )
