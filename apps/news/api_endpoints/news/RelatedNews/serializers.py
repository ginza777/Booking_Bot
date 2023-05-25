from rest_framework.serializers import ModelSerializer

from apps.news.models import News


class RelatedNewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = ("id", "title", "banner", "slug", "published_at")
