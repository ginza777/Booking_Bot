from rest_framework.generics import CreateAPIView, ListAPIView

from .serializers import VisitorSerializer, ChoiceOfServiceSerializer, ActivityOfYourCompanySerializer
from apps.application.models import Visitor, ChoiceOfService, ActivityOfYourCompany


class VisitorCreateAPIView(CreateAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer


class ChoiceOfServiceListAPIView(ListAPIView):
    queryset = ChoiceOfService.objects.all()
    serializer_class = ChoiceOfServiceSerializer


class ActivityOfYourCompanyListAPIView(ListAPIView):
    queryset = ActivityOfYourCompany.objects.all()
    serializer_class = ActivityOfYourCompanySerializer
