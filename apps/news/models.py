from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import get_language
from django.utils.translation import gettext_lazy as _
from unidecode import unidecode
from django_resized import ResizedImageField

from apps.common.models import BaseModel


class Slugify(models.Model):
    slug = models.SlugField(_("slug"), max_length=255, unique=True, null=True, blank=True)
    SLUG_FROM_FIELD = None

    class Meta:
        abstract = True

    def _make_slug(self, value):
        if value is not None:
            original_slug = slugify(unidecode(value))
            unique_slug = original_slug
            num = 1
            while self.__class__.objects.exclude(pk=self.pk).filter(slug=unique_slug).exists():
                unique_slug = f"{original_slug}-{num}"
                num += 1
            return slugify(unique_slug)

    def save(self, *args, **kwargs):
        if self.slug is None:
            value_for_slug = getattr(self, self.SLUG_FROM_FIELD)
            self.slug = self._make_slug(value_for_slug)
        return super().save(*args, **kwargs)


class MultiLangSlugify(Slugify):
    slug_from_lang = models.CharField(
        choices=settings.LANGUAGES,
        max_length=64,
        verbose_name=_("select the language of the slug"),
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.slug_from_lang is not None:
            value_for_slug = getattr(self, f"{self.SLUG_FROM_FIELD}_{self.slug_from_lang}")
            self.slug = self._make_slug(value_for_slug)

        if self.slug is None and self.slug_from_lang is None:
            self.slug_from_lang = get_language()
        return super().save(*args, **kwargs)


class News(BaseModel, MultiLangSlugify):
    title = models.CharField(_("Title"), max_length=255)
    description = models.CharField(_("Description"), max_length=256, null=True)
    banner = ResizedImageField(upload_to=_("banner/"), verbose_name=_("Banner"), quality=100)
    content = RichTextUploadingField(_("Content"))
    SLUG_FROM_FIELD = "title"  # type: ignore # noqa: F401
    published_at = models.DateField(_("Published at"))

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-published_at"]
        verbose_name = _("News")
        verbose_name_plural = _("News")


class Folder(BaseModel):
    name = models.CharField(_("Name"), max_length=255)
    image = ResizedImageField(upload_to="folder/", verbose_name=_("Image"), null=True, quality=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Folder")
        verbose_name_plural = _("Folders")


class Gallery(BaseModel):
    folder = models.ForeignKey(Folder, verbose_name=_("Name"), on_delete=models.CASCADE)
    name = models.CharField(_("Name"), max_length=255)
    image = ResizedImageField(upload_to="gallery/", verbose_name=_("Image"), quality=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Gallery")
        verbose_name_plural = _("Galleries")


class StaticPage(BaseModel, MultiLangSlugify):
    title = models.CharField(_("Title"), max_length=255)
    body = RichTextUploadingField(_("Body"))
    SLUG_FROM_FIELD = "title"  # type: ignore # noqa: F401

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Static Page")
        verbose_name_plural = _("Static Pages")
