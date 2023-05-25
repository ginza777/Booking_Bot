from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.main.api_endpoints.main_banner.MainBanner.serializers import \
    MainBannerSerializer
from apps.main.models import MainBanner


class MainBannerAPIView(APIView):
    def get(self, request):
        queryset = MainBanner.objects.first()
        if not queryset:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        serializer = MainBannerSerializer(queryset, context={"request": self.request})
        return Response(serializer.data)


__all__ = ("MainBannerAPIView",)
