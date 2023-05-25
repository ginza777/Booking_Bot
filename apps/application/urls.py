from rest_framework.urls import path

from .api_endpoints import (ActivityOfYourCompanyListAPIView,
                            BookStandCreateAPIView, ChoiceOfServiceListAPIView,
                            HearingUsListAPIView, RetrieveVisitorTicketAPIView,
                            VisitorCreateAPIView)
from .views import ticket

urlpatterns = [
    path("BookStandCreate", BookStandCreateAPIView.as_view(), name="BookStandCreate"),
    path("HearingUsList", HearingUsListAPIView.as_view(), name="HearingUsList"),
    path("VisitorCreate", VisitorCreateAPIView.as_view(), name="VisitorCreate"),
    path("ChoiceOfServiceList", ChoiceOfServiceListAPIView.as_view(), name="ChoiceOfServiceList"),
    path("ActivityOfYourCompanyList", ActivityOfYourCompanyListAPIView.as_view(), name="ActivityOfYourCompanyList"),
    path("VisitorDetail/<int:pk>", RetrieveVisitorTicketAPIView.as_view(), name="VisitorCreate"),
    path("tick/", ticket, name="ticket"),
]
