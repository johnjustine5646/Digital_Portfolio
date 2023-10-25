from django.apps import AppConfig


class KichusiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Kichusite'
    def ready(self):
        import Kichusite.signals
        