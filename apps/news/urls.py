from django.urls import path

from apps.news.api_endpoints.folder.FolderList import FolderListAPIView
from apps.news.api_endpoints.gallery.GalleryList import GalleryListAPIView
from apps.news.api_endpoints.news.NewsDetail import NewsDetailAPIView
from apps.news.api_endpoints.news.NewsList import NewsListAPIView
from apps.news.api_endpoints.static_page import StaticPageListAPIView
from apps.news.api_endpoints.static_page.StaticPageDetail import \
    StaticPageDetailAPIView
from apps.news.api_endpoints.news.RelatedNews import RelatedNewsAPIView

urlpatterns = [
    path("NewsList", NewsListAPIView.as_view(), name="news-list"),
    path("StaticPageList", StaticPageListAPIView.as_view(), name="static-page-list"),
    path("<slug:slug>/NewsDetail", NewsDetailAPIView.as_view(), name="news-detail"),
    path("<slug:slug>/StaticPageDetail", StaticPageDetailAPIView.as_view(), name="static-page-detail"),
    path("FolderList", FolderListAPIView.as_view(), name="folder-list"),
    path("<int:pk>/GalleryList", GalleryListAPIView.as_view(), name="gallery-list"),
    path("<int:pk>/RelatedNews", RelatedNewsAPIView.as_view(), name="related-news"),
]
