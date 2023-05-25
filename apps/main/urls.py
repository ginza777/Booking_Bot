from django.urls import path

from apps.main.api_endpoints.about_project import AboutProjectListAPIView
from apps.main.api_endpoints.about_us import AboutUsAPIView
from apps.main.api_endpoints.benifits_for_visitor import \
    BenifitsForVisitorListAPIView
from apps.main.api_endpoints.contact import ContactAPIView
from apps.main.api_endpoints.contact_us import ContactUsAPIView
from apps.main.api_endpoints.exhibitor import ExhibitorListAPIView
from apps.main.api_endpoints.main_banner import MainBannerAPIView
from apps.main.api_endpoints.participant import ParticipantListAPIView
from apps.main.api_endpoints.partner import PartnerListAPIView
from apps.main.api_endpoints.product_group import ProductGroupListAPIView
from apps.main.api_endpoints.social import SocialAPIView
from apps.main.api_endpoints.team import TeamListAPIView

urlpatterns = [
    path("Banner", MainBannerAPIView.as_view(), name="main-banner"),
    path("AboutProjectList", AboutProjectListAPIView.as_view(), name="about-project-list"),
    path("ParticipantList", ParticipantListAPIView.as_view(), name="participant"),
    path("ExhibitorList", ExhibitorListAPIView.as_view(), name="exhibitor"),
    path("AboutUs", AboutUsAPIView.as_view(), name="about-us"),
    path("ProductGroupList", ProductGroupListAPIView.as_view(), name="product-group"),
    path("TeamList", TeamListAPIView.as_view(), name="team"),
    path("BenifitsForVisitorList", BenifitsForVisitorListAPIView.as_view(), name="benifits-for-visitor"),
    path("PartnerList", PartnerListAPIView.as_view(), name="partner"),
    path("Contact", ContactAPIView.as_view(), name="contact"),
    path("ContactUs", ContactUsAPIView.as_view(), name="contact-us"),
    path("Social", SocialAPIView.as_view(), name="social"),
]
