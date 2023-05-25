from rest_framework.serializers import ModelSerializer

from apps.main.models import Contact


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ("id", "email", "address", "phone", "latitude", "longitude")
