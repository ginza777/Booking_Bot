from rest_framework.generics import ListAPIView

from apps.main.api_endpoints.about_project.AboutProjectList.serializers import \
    AboutProjectSerializer
from apps.main.models import AboutProject


class AboutProjectListAPIView(ListAPIView):
    serializer_class = AboutProjectSerializer

    def get_queryset(self):
        return AboutProject.objects.all().order_by("order")


__all__ = ("AboutProjectListAPIView",)
