import requests
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

from apps.application.choices import PersonalityOption
from apps.common.models import BaseModel


class HearingUs(BaseModel):
    title = models.CharField(_("Title"), max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Hearing Us")
        verbose_name_plural = _("Hearing Us")


class BookStand(BaseModel):
    name = models.CharField(_("Name"), max_length=255)
    company_name = models.CharField(_("Company name"), max_length=255)
    country = models.ForeignKey("common.Country", verbose_name=_("Country"), on_delete=models.CASCADE)
    phone = PhoneNumberField(_("Phone"), null=True, blank=True)
    email = models.EmailField(_("Email"), max_length=255)
    hear_us = models.ForeignKey(HearingUs, on_delete=models.CASCADE, verbose_name=_("Hearing us"),null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Book Stand")
        verbose_name_plural = _("Book Stands")


class ChoiceOfService(BaseModel):
    title = models.CharField(_("First name"), max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Choice Of Service")
        verbose_name_plural = _("Choice Of Services")


class ActivityOfYourCompany(BaseModel):
    title = models.CharField(_("First name"), max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Activity Of Your Company")
        verbose_name_plural = _("Activity Of Your Companies")


class Visitor(BaseModel):
    first_name = models.CharField(_("First name"), max_length=100)
    last_name = models.CharField(_("Last name"), max_length=100)
    country = models.ForeignKey("common.Country", verbose_name=_("Country"), on_delete=models.CASCADE)
    region = models.ForeignKey("common.Region", verbose_name=_("Region"), on_delete=models.CASCADE)
    personality = models.CharField(
        verbose_name=_("Personality"),
        max_length=10,
        choices=PersonalityOption.choices,
        default=PersonalityOption.PHYSICAL,
    )
    company_name = models.CharField(_("Company name"), max_length=100, null=True, blank=True)
    job_title = models.CharField(_("Job title"), max_length=100, null=True, blank=True)
    website = models.URLField(_("Website"), null=True, blank=True)
    phone = PhoneNumberField(_("Phone"))
    email = models.EmailField(_("Email"), max_length=255)
    service = models.ManyToManyField(ChoiceOfService, verbose_name=_("Services"), null=True)
    activity = models.ManyToManyField(ActivityOfYourCompany, verbose_name=_("Activities"), null=True)
    feedback = models.TextField(_("Feedback"), null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Visitor")
        verbose_name_plural = _("Visitors")


class Ticket(BaseModel):
    visitor = models.OneToOneField(
        Visitor, on_delete=models.CASCADE, verbose_name=_("Visitor"), related_name="visitor_ticket"
    )
    pdf = models.FileField(upload_to="ticket", verbose_name=_("Ticket"))

    def __str__(self):
        return self.visitor.first_name

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Ticket")
        verbose_name_plural = _("Tickets")


class TicketInfo(BaseModel):
    date = models.CharField(_("Date"), max_length=100)
    time = models.CharField(_("Time"), max_length=100)
    address = models.CharField(_("Address"), max_length=255)

    def __str__(self):
        return self.date

    class Meta:
        verbose_name = _("Ticket Info")
        verbose_name_plural = _("Ticket Info")


@receiver(post_save, sender=BookStand)
def save_contact_us(sender, instance, *args, **kwargs):
    try:
        text = (
            "Book a Stand!\n\n"
            f"*Name:* {instance.name}\n"
            f"*Country:* {instance.country.name}\n"
            f"*Company Name:* {instance.company_name}\n"
            f"*Phone Number:* {instance.phone}\n"
            f"*Email:* {instance.email}\n"
            f"*Hear Us:* {instance.hear_us}"
        )

        url = f"https://api.telegram.org/bot{settings.API_KEY}" + "/sendMessage"

        requests.get(url, data={"chat_id": settings.CHAT_ID, "text": text, "parse_mode": "Markdown"})

    except Exception as e:
        print(e)


@receiver(post_save, sender=Visitor)
def save_contact_us(sender, instance, *args, **kwargs):
    try:
        text = (
            "Visitor!\n\n"
            f"*Firstname:* {instance.first_name}\n"
            f"*Lastname:* {instance.last_name}\n"
            f"*Country:* {instance.country.name}\n"
            f"*Region:* {instance.region.name}\n"
            f"*Personality:* {instance.personality}\n"
            f"*Company Name:* {instance.company_name}\n"
            f"*Job Title:* {instance.job_title}\n"
            f"*Website:* {instance.website}\n"
            f"*Phone Number:* {instance.phone}\n"
            f"*Email:* {instance.email}\n"
            f"*Feedback:* {instance.feedback}\n"
        )

        url = f"https://api.telegram.org/bot{settings.API_KEY}" + "/sendMessage"

        requests.get(url, data={"chat_id": settings.CHAT_ID, "text": text, "parse_mode": "Markdown"})

    except Exception as e:
        print(e)
