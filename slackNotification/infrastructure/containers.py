from dependency_injector import containers, providers

from slackNotification.application.service.NotifySalesUseCase import NotifySalesUseCase
from slackNotification.infrastructure.SalesConsumer import SalesConsumer
from slackNotification.infrastructure.repository.FakeSlackSender import FakeSlackSender


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    slack_sender = providers.Factory(
        FakeSlackSender
    )

    notify_sales_use_case = providers.Factory(
        NotifySalesUseCase,
        slack_sender,
        config.SLACK_ADDRESS,
        config.SALES_SLACK_CHANNEL
    )

    sales_consumer = providers.Factory(
        SalesConsumer,
        notify_sales_use_case
    )
