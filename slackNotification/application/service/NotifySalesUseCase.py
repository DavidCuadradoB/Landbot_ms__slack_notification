from slackNotification.application.command.NotifySalesCommand import NotifySalesCommand
from slackNotification.application.dto.SlacklDTO import SlackDTO
from slackNotification.application.repository.SlackSender import SlackSender


class NotifySalesUseCase:

    def __init__(self, slack_sender: SlackSender, slack_address, slack_channel):
        self.slack_sender = slack_sender
        self.slack_address = slack_address
        self.slack_channel = slack_channel

    def execute(self, command: NotifySalesCommand):
        slack_dto = SlackDTO(command.topic, command.description, self.slack_channel, self.slack_address)
        self.slack_sender.send(slack_dto)
