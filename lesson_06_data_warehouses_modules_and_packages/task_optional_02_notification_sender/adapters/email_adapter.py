from adapters.message_sender import MessageSender

from services.email_service import EmailService


class EmailAdapter(MessageSender):
    """
    Sending email
    """

    def __init__(self, email_service: EmailService, email_address):
        self.email_service = email_service
        self.email_address = email_address

    def send_message(self, message: str):
        """
        :param message:
        :return:
        """
        self.email_service.send_email(self.email_address, message)
