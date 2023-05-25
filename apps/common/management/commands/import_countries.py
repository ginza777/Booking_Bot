import json

from django.core.management.base import BaseCommand, CommandError
from modeltranslation.utils import build_localized_fieldname

from ...models import Country


class Command(BaseCommand):
    help = "Import countries from a JSON file"

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.HTTP_NOT_MODIFIED(
                "Import countries... wait...",
            )
        )
        # Country.objects.all().delete()
        try:
            with open(
                "apps/common/management/source/country_data.json",
                "r",
            ) as json_file:
                data = json.load(json_file)
                i = 0
                for item in data:
                    country = Country.objects.create(name=item["name_english"])
                    field_name_ru = build_localized_fieldname("name", "ru")
                    setattr(country, field_name_ru, item["name_russian"])
                    field_name_uz = build_localized_fieldname("name", "uz")
                    setattr(country, field_name_uz, item["name_uzbek"])
                    country.save()
                    i += 1
        except FileNotFoundError as e:
            raise CommandError("File country JSON doesn't exist") from e

        self.stdout.write(self.style.SUCCESS(f"{str(i)} countries successfully imported"))
