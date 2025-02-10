from app.models.notification import Notification


class NotificationList:
    def __init__(self):
        self.notifications = {}

    def create_notification(self, notification_id, status, text, time):
        """Создание нового уведомления."""
        if notification_id in self.notifications:
            raise ValueError("Уведомление с таким ID уже существует.")
        self.notifications[notification_id] = Notification(notification_id, status, text, time)
    
    def send_notification(self, notification_id):
        """Отправка уведомления пользователю."""
        if notification_id not in self.notifications:
            raise ValueError("Уведомление не найдено.")
        notification = self.notifications[notification_id]
        print(f"Отправка уведомления: {notification.text} ")
        notification.status = "sent"
    
    def update_notification_status(self, notification_id, status):
        """Обновление статуса уведомления."""
        if notification_id not in self.notifications:
            raise ValueError("Уведомление не найдено.")
        self.notifications[notification_id].status = status

    def list_notifications(self):
        """Вывода всех уведомлений."""
        if not self.notifications:
            print("Нет зарегистрированных уведомлений.")
        else:
            print("Уведомления:")
            for notification in self.notifications.values():
                print(notification)