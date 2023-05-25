from rest_framework.serializers import ModelSerializer

from apps.news.models import StaticPage


class StaticPageSerializer(ModelSerializer):
    class Meta:
        model = StaticPage
        fields = (
            "id",
            "title",
            "slug",
        )
