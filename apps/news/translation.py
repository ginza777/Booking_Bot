from modeltranslation.translator import TranslationOptions, register

from .models import Folder, Gallery, News, StaticPage


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ("title", "description", "content")


@register(Folder)
class FolderTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Gallery)
class GalleryTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(StaticPage)
class StaticPageTranslationOptions(TranslationOptions):
    fields = ("title", "body")
