from django.apps import AppConfig


class BigBlueButtonAppConfig(AppConfig):
    name = 'django_bigbluebutton'
    verbose_name = "Meeting App"

    def ready(self):
        import django_bigbluebutton.signals

