from django.apps import AppConfig


class ApplicationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.application"

    def ready(self):
        import apps.application.signals  # noqa
