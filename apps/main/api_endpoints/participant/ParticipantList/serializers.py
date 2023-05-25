from rest_framework.serializers import ModelSerializer

from apps.common.models import Country
from apps.main.models import Participant


class CountSerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "name")


class ParticipantSerializer(ModelSerializer):
    country = CountSerializer(read_only=True)

    class Meta:
        model = Participant
        fields = ("id", "title", "country", "image", "link")
