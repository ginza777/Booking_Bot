from rest_framework.generics import ListAPIView

from apps.main.api_endpoints.participant.ParticipantList.serializers import \
    ParticipantSerializer
from apps.main.models import Participant


class ParticipantListAPIView(ListAPIView):
    serializer_class = ParticipantSerializer

    def get_queryset(self):
        return Participant.objects.all().order_by("order")


__all__ = ("ParticipantListAPIView",)
