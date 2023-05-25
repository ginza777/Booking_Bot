from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.main.api_endpoints.about_us.AboutUs.serializers import \
    AboutUsSerializer
from apps.main.models import AboutUs


class AboutUsAPIView(APIView):
    def get(self, request):
        queryset = AboutUs.objects.all().first()
        if not queryset:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        serializer = AboutUsSerializer(queryset, context={"request": self.request})
        return Response(serializer.data)


__all__ = ("AboutUsAPIView",)
