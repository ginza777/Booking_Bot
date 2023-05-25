from django.urls import path

from apps.common.api_endpoints.country import CountryListAPIView
from apps.common.api_endpoints.region import RegionListAPIView

urlpatterns = [
    path("CountryList", CountryListAPIView.as_view(), name="country-list"),
    path("<int:pk>/RegionList", RegionListAPIView.as_view(), name="region-list"),
]
