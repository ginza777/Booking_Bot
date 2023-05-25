from rest_framework.serializers import ModelSerializer

from apps.main.models import AboutProject


class AboutProjectSerializer(ModelSerializer):
    class Meta:
        model = AboutProject
        fields = ("id", "name", "count")
