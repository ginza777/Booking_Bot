from rest_framework.generics import ListAPIView

from apps.main.api_endpoints.team.TeamList.serializers import TeamSerializer
from apps.main.models import Team


class TeamListAPIView(ListAPIView):
    serializer_class = TeamSerializer

    def get_queryset(self):
        return Team.objects.all().order_by("order")


__all__ = ("TeamListAPIView",)
