from abc import ABC, abstractmethod

from slackNotification.application.dto.SlackDTO import SlackDTO


class SlackSender(ABC):
    @abstractmethod
    def send(self, slack_dto: SlackDTO):
        pass
