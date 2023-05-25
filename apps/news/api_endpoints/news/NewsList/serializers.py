from rest_framework.serializers import ModelSerializer

from apps.news.models import News


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = ("id", "title", "description", "banner", "slug", "published_at")
