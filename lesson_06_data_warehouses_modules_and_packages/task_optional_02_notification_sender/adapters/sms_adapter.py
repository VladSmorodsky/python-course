from adapters.message_sender import MessageSender

from services.sms_service import SMSService


class SMSAdapter(MessageSender):
    """
    Sending SMS
    """

    def __init__(self, sms_service: SMSService, phone_number: str) -> None:
        """
        :param sms_service:
        :param phone_number:
        """
        self.sms_service = sms_service
        self.phone_number = phone_number

    def send_message(self, message: str) -> None:
        """
        :param message:
        :return:
        """
        self.sms_service.send_sms(self.phone_number, message)
