from rest_framework.serializers import ModelSerializer

from apps.main.models import ContactUs


class ContactUsSerializer(ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ("id", "name", "country", "company_name", "phone", "message")
