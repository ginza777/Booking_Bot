from django.contrib import admin

from ..common.admin_mixin import TabbedTranslationAdmin
from .models import (ActivityOfYourCompany, BookStand, ChoiceOfService,
                     HearingUs, Ticket, TicketInfo, Visitor)


@admin.register(HearingUs)
class HearingUsModelAdmin(TabbedTranslationAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")


@admin.register(BookStand)
class BookStandModelAdmin(TabbedTranslationAdmin):
    list_display = ("id", "name", "country", "phone", "email", "hear_us", "created_at")
    list_display_links = ("id", "name")
    search_fields = ("name", "phone", "email")
    list_filter = ("country", "hear_us", "created_at")

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(ChoiceOfService)
class ChoiceOfServiceModelAdmin(TabbedTranslationAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")


@admin.register(ActivityOfYourCompany)
class ActivityOfYourCompanyModelAdmin(TabbedTranslationAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "personality", "phone", "email", "created_at")
    list_display_links = ("id", "first_name")
    list_filter = ("personality", "country", "region", "created_at")
    search_fields = ("first_name", "last_name", "phone", "email")

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "visitor", "pdf")
    list_display_links = ("id", "visitor")


@admin.register(TicketInfo)
class TicketInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "time", "address")
    list_display_links = ("id", "date")

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        return True
