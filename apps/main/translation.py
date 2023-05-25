from modeltranslation.translator import TranslationOptions, register

from .models import (AboutProject, AboutUs, BenifitsForVisitor, Contact,
                     Exhibitor, MainBanner, Participant, ProductGroup, Team)


@register(MainBanner)
class MainBannerTranslationOptions(TranslationOptions):
    fields = ("title", "sub_title")


@register(AboutProject)
class AboutProjectTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ("text",)


@register(Participant)
class ParticipantTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(Exhibitor)
class ExhibitorTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(ProductGroup)
class ProductGroupTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(Team)
class TeamTranslationOptions(TranslationOptions):
    fields = ("full_name", "position")


@register(BenifitsForVisitor)
class BenifitsForVisitorTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ("address",)
