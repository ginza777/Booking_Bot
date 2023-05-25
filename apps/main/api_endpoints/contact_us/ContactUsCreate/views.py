from rest_framework.generics import CreateAPIView

from apps.main.api_endpoints.contact_us.ContactUsCreate.serializers import ContactUsSerializer
from apps.main.models import ContactUs


class ContactUsAPIView(CreateAPIView):
    serializer_class = ContactUsSerializer
    queryset = ContactUs.objects.all()


__all__ = ("ContactUsAPIView",)
