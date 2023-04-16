from unittest import TestCase

import mockito
from mockito import when

from slackNotification.application.command.NotifySalesCommand import NotifySalesCommand
from slackNotification.application.repository.SlackSender import SlackSender
from slackNotification.application.service.NotifySalesUseCase import NotifySalesUseCase


class NotifySalesUseCaseTest(TestCase):
    def test_execute_should_call_event_sender(self):
        a_topic = "A topic"
        a_description = "A description"
        email_sender_mock = mockito.mock(SlackSender)
        when(email_sender_mock).send(mockito.any()).thenReturn(mockito.any())
        notify_sales_use_case = NotifySalesUseCase(email_sender_mock, 'an slack address', "an slack channel")
        notify_sales_command = NotifySalesCommand(a_topic, a_description)
        notify_sales_use_case.execute(notify_sales_command)
        mockito.verify(email_sender_mock).send(mockito.any())
