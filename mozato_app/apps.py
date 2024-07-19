from django.apps import AppConfig


class MozatoAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mozato_app'

    def ready(self):
        import mozato_app.signals