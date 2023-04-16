from django.apps import AppConfig

from slackNotification import container


class SlacknotificationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'slackNotification'

    def ready(self):
        container.wire(modules=[".views"])
