from rest_framework.serializers import ModelSerializer

from apps.news.models import News


class NewsDetailSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = ("id", "title", "banner", "content", "published_at")
