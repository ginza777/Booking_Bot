from django.contrib import admin

from apps.common.admin_mixin import TabbedTranslationAdmin
from apps.common.models import Country, Region


@admin.register(Country)
class CountryModelAdmin(TabbedTranslationAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


@admin.register(Region)
class RegionModelAdmin(TabbedTranslationAdmin):
    list_display = ("id", "name", "country")
    list_display_links = ("id", "name")
    list_filter = ("country",)
