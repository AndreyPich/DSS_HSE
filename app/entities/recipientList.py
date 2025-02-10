from app.models.recipient import Recipient


class RecipientList:
    def __init__(self):
        self.recipients = {}

    def register_recipient(self, recipient_id, location, contact):
        """Регистрация получателя уведомлений."""
        if recipient_id in self.recipients:
            raise ValueError("Получатель с таким ID уже зарегистрирован.")
        self.recipients[recipient_id] = Recipient(recipient_id, location, contact)
    
    def update_recipient(self, recipient_id, location=None, contact=None):
        """Обновление данных получателя."""
        if recipient_id not in self.recipients:
            raise ValueError("Получатель не найден.")
        recipient = self.recipients[recipient_id]
        if location:
            recipient.location = location
        if contact:
            recipient.contact = contact

    def list_recipients(self):
        """Вывода всех получателей."""
        if not self.recipients:
            print("Нет зарегистрированных получателей.")
        else:
            print("Получатели:")
            for recipient in self.recipients.values():
                print(recipient)