from adapters.message_sender import MessageSender

from services.push_service import PushService


class PushAdapter(MessageSender):
    """
    Sending push notification
    """

    def __init__(self, push_service: PushService, device_id: str) -> None:
        """
        :param push_service:
        :param device_id:
        """
        self.push_service = push_service
        self.device_id = device_id

    def send_message(self, message: str) -> None:
        """
        :param message:
        :return:
        """
        self.push_service.send_push(self.device_id, message)
