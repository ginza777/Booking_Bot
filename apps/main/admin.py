from django.contrib import admin

from apps.common.admin_mixin import TabbedTranslationAdmin
from apps.main.models import (AboutProject, AboutUs, BenifitsForVisitor,
                              Contact, ContactUs, Exhibitor, MainBanner,
                              Participant, Partner, ProductGroup, Social, Team)


@admin.register(MainBanner)
class MainBannerModelAdmin(TabbedTranslationAdmin):
    list_display = ("id", "title", "sub_title", "arranged_date")
    list_display_links = ("id", "title")

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        return True


@admin.register(AboutProject)
class AboutProjectModelAdmin(TabbedTranslationAdmin):
    list_display = ("id", "name", "count", "order", "created_at")
    list_display_links = ("id", "name")
    list_filter = ("created_at",)
    search_fields = ("name",)


@admin.register(AboutUs)
class AboutUsModelAdmin(TabbedTranslationAdmin):
    list_display = ("id", "text")
    list_display_links = ("id", "text")

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        return True


@admin.register(Participant)
class ParticipantModelAdmin(TabbedTranslationAdmin):
    list_display = ("id", "title", "country", "order")
    list_display_links = ("id", "title")
    list_filter = ("country",)
    search_fields = ("title",)


@admin.register(Exhibitor)
class ExhibitorModelAdmin(TabbedTranslationAdmin):
    list_display = ("id", "title", "country", "order")
    list_display_links = ("id", "title")
    list_filter = ("country",)
    search_fields = ("title",)


@admin.register(ProductGroup)
class ProductGroupModelAdmin(TabbedTranslationAdmin):
    list_display = ("id", "title", "description", "order")
    list_display_links = ("id", "title")
    search_fields = ("title",)


@admin.register(Team)
class TeamModelAdmin(TabbedTranslationAdmin):
    list_display = ("id", "full_name", "position", "order")
    list_display_links = ("id", "full_name")
    search_fields = ("full_name", "position")


@admin.register(BenifitsForVisitor)
class BenifitsForVisitorModelAdmin(TabbedTranslationAdmin):
    list_display = ("id", "title", "description", "order")
    list_display_links = ("id", "title")
    search_fields = ("title",)


@admin.register(Partner)
class PartnerModelAdmin(TabbedTranslationAdmin):
    list_display = ("id", "link", "image", "order")
    list_display_links = ("id", "link")


@admin.register(Contact)
class ContactModelAdmin(TabbedTranslationAdmin):
    list_display = ("id", "email", "address", "phone", "latitude", "longitude")
    list_display_links = ("id", "email")

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        return True


@admin.register(ContactUs)
class ContactUsModelAdmin(TabbedTranslationAdmin):
    list_display = ("id", "name", "country", "company_name", "phone", "message", "created_at")
    list_display_links = ("id", "name")
    list_filter = ("country", "created_at")
    search_fields = ("name", "company_name", "phone")

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Social)
class SocialModelAdmin(TabbedTranslationAdmin):
    list_display = ("id", "telegram", "instagram", "twitter", "youtube")
    list_display_links = ("id", "telegram")

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        return True
