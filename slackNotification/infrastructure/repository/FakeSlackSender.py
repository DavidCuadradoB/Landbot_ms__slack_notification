from slackNotification.application.dto.SlackDTO import SlackDTO
from slackNotification.application.repository.SlackSender import SlackSender


class FakeSlackSender(SlackSender):

    def send(self, slack_dto: SlackDTO):
        print("Sending ---Slack--- with topic %s and description %s to the slack address %s and channel %s"
              % (slack_dto.topic, slack_dto.description, slack_dto.slack_address, slack_dto.slack_channel))
        print("Slack sent")
