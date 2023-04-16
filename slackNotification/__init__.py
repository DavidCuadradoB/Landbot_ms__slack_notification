from Landbot_ms__slack_notification import settings
from slackNotification.infrastructure.containers import Container

container = Container()
container.config.from_dict(settings.__dict__)
