from exceptions.sms_sending_error import SMSSendingError


class SMSService:
    """
    Send with sms notification
    """

    def send_sms(self, phone_number: str, message: str) -> None:
        """
        :param phone_number:
        :param message:
        :return:
        """
        try:
            print(f"Відправка SMS на {phone_number}: {message}")
        except Exception:
            raise SMSSendingError(f"SMS is not sent to {phone_number}.")
