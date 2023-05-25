from rest_framework.serializers import ModelSerializer

from apps.main.models import BenifitsForVisitor


class BenifitsForVisitorSerializer(ModelSerializer):
    class Meta:
        model = BenifitsForVisitor
        fields = ("id", "title", "description", "icon")
