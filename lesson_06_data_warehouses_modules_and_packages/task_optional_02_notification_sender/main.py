from adapters.sms_adapter import SMSAdapter
from adapters.email_adapter import EmailAdapter
from adapters.push_adapter import PushAdapter
from strategies.notification_strategy import NotificationStrategy
from services.sms_service import SMSService
from services.email_service import EmailService
from services.push_service import PushService

# Використання

sms_service = SMSService()
email_service = EmailService()
push_service = PushService()

# Відправка повідомлень через різні сервіси за допомогою адаптерів
message = "Привіт! Це тестове повідомлення."

notification_strategy = NotificationStrategy(SMSAdapter(sms_service, "+380123456789"))
notification_strategy.send_message(message)

notification_strategy.notification_adapter = EmailAdapter(email_service, "user@example.com")
notification_strategy.send_message(message)

notification_strategy.notification_adapter = PushAdapter(push_service, "device123")
notification_strategy.send_message(message)
