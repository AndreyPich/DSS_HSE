# Модель для получателя
class Recipient:
    def __init__(self, recipient_id, location, contact):
        self.recipient_id = recipient_id
        self.location = location
        self.contact = contact

    def __repr__(self):
        return f"ID: {self.recipient_id}, Локация: {self.location}, Контакт: {self.contact}"