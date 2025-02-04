from exceptions.push_sending_error import PushSendingError


class PushService:
    """
    Send with push notification
    """

    def send_push(self, device_id: str, message: str) -> None:
        """
        :param device_id:
        :param message:
        :return:
        """
        try:
            print(f"Відправка Push-повідомлення на пристрій {device_id}: {message}")
        except Exception:
            raise PushSendingError(f"Push is not sent to {device_id}.")
