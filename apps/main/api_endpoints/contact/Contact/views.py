from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.main.api_endpoints.contact.Contact.serializers import \
    ContactSerializer
from apps.main.models import Contact


class ContactAPIView(APIView):
    def get(self, request):
        queryset = Contact.objects.all().first()
        if not queryset:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        serializer = ContactSerializer(queryset, context={"request": self.request})
        return Response(serializer.data)


__all__ = ("ContactAPIView",)
