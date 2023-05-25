from modeltranslation.translator import TranslationOptions, register

from .models import Country, Region


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ("name",)
