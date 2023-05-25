from rest_framework.serializers import ModelSerializer

from apps.main.models import Social


class SocialSerializer(ModelSerializer):
    class Meta:
        model = Social
        fields = ("id", "telegram", "instagram", "twitter", "youtube")
