import random
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import RelatedNewsSerializer
from apps.news.models import News


class RelatedNewsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        news = News.objects.exclude(id=kwargs['pk']).order_by('?')
        serializer = RelatedNewsSerializer(instance=news, many=True, context={'request': request}).data
        return Response(serializer, status=200)