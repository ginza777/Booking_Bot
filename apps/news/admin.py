from django.contrib import admin

from apps.common.admin_mixin import TabbedTranslationAdmin
from apps.news.models import Folder, Gallery, News, StaticPage


@admin.register(News)
class NewsModelAdmin(TabbedTranslationAdmin):
    list_display = ("id", "title", "published_at")
    list_display_links = ("id", "title")
    list_filter = ("published_at",)
    search_fields = ("title",)


@admin.register(Folder)
class FolderModelAdmin(TabbedTranslationAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


@admin.register(Gallery)
class GalleryModelAdmin(TabbedTranslationAdmin):
    list_display = ("id", "name", "folder", "created_at")
    list_display_links = ("id", "name")
    list_filter = ("folder", "created_at")
    search_fields = ("name",)


@admin.register(StaticPage)
class StaticPageModelAdmin(TabbedTranslationAdmin):
    list_display = ("id", "title", "slug")
    list_display_links = ("id", "title")
    search_fields = ("title",)
