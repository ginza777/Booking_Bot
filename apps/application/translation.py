from modeltranslation.translator import TranslationOptions, register

from .models import ActivityOfYourCompany, ChoiceOfService, HearingUs


@register(HearingUs)
class HearingUsTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(ChoiceOfService)
class ChoiceOfServiceTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(ActivityOfYourCompany)
class ActivityOfYourCompanyTranslationOptions(TranslationOptions):
    fields = ("title",)
