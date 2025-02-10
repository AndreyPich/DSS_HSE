# Модель для уведомления
class Notification:
    def __init__(self, notification_id, status, text, time):
        self.notification_id = notification_id
        self.status = status
        self.text = text
        self.time = time

    def __repr__(self):
        return (f"ID: {self.notification_id}, Статус: {self.status}, "
                f"Текст: {self.text}, Время: {self.time}")