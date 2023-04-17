import pickle

import json

from dependency_injector.wiring import Provide, inject
from kafka import KafkaConsumer

from slackNotification.application.command.NotifySalesCommand import NotifySalesCommand
from slackNotification.application.service.NotifySalesUseCase import NotifySalesUseCase


class SalesConsumer:

    def __init__(self, notify_sales_use_case: NotifySalesUseCase):
        self.notify_sales_use_case = notify_sales_use_case

    def consume(self):
        consumer = KafkaConsumer('sales',
                                 bootstrap_servers=['kafka:29092'],
                                 api_version=(0, 10)
                                 # ,consumer_timeout_ms=1000
                                 )

        for message in consumer:
            print(message.value)
            body = json.loads(message.value)
            command = NotifySalesCommand(body['topic'], body['description'])
            self.notify_sales_use_case.execute(command)
