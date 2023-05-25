from rest_framework.serializers import ModelSerializer

from apps.main.models import Team


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = ("id", "full_name", "position", "image")
