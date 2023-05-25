from rest_framework.serializers import ModelSerializer

from apps.main.api_endpoints.participant.ParticipantList.serializers import \
    CountSerializer
from apps.main.models import Exhibitor


class ExhibitorSerializer(ModelSerializer):
    country = CountSerializer(read_only=True)

    class Meta:
        model = Exhibitor
        fields = ("id", "title", "country", "image", "link")
