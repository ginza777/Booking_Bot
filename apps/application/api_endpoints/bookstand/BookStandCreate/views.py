from rest_framework.generics import CreateAPIView, ListAPIView

from .serializers import BookStandSerializer, HearingUsSerializer
from apps.application.models import BookStand, HearingUs


class BookStandCreateAPIView(CreateAPIView):
    queryset = BookStand.objects.all()
    serializer_class = BookStandSerializer


class HearingUsListAPIView(ListAPIView):
    queryset = HearingUs.objects.all()
    serializer_class = HearingUsSerializer
