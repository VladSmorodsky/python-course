from exceptions.email_sending_error import EmailSendingError


class EmailService:
    """
    Send with email notification
    """

    def send_email(self, email_address: str, message: str) -> None:
        """
        :param email_address:
        :param message:
        :return:
        :raise EmailSendingError
        """
        try:
            print(f"Відправка Email на {email_address}: {message}")
        except Exception:
            raise EmailSendingError(f"Email is not sent to {email_address}.")
