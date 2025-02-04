from adapters.message_sender import MessageSender


class NotificationStrategy:
    """
    Class used for sending notifications from different adapters
    """

    def __init__(self, notification_adapter: MessageSender) -> None:
        self._notification_adapter = notification_adapter

    @property
    def notification_adapter(self) -> MessageSender:
        """
        :return:
        :rtype MessageSender:
        """
        return self._notification_adapter

    @notification_adapter.setter
    def notification_adapter(self, notification_adapter: MessageSender) -> None:
        """
        :param notification_adapter:
        :return:
        """
        self._notification_adapter = notification_adapter

    def send_message(self, message: str) -> None:
        """
        :param message:
        :return:
        """
        try:
            self._notification_adapter.send_message(message)
        except Exception as error:
            print(error)
