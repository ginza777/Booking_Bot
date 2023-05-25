from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.main.api_endpoints.social.Social.serializers import SocialSerializer
from apps.main.models import Social


class SocialAPIView(APIView):
    def get(self, request):
        queryset = Social.objects.all().first()
        if not queryset:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        serializer = SocialSerializer(queryset, context={"request": self.request})
        return Response(serializer.data)


__all__ = ("SocialAPIView",)
