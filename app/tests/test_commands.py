from app.entities.eventList import EventList
from app.entities.notificationList import NotificationList
from app.entities.recipientList import RecipientList


def test_create_event():
    events = EventList()
    events.create_event(1, "Пожар", 5)
    events.assign_location(1, "Москва")
    assert 1 in events.events
    assert events.events[1].event_type == "Пожар"
    assert events.events[1].danger_level == 5
    assert events.events[1].location == "Москва"


def test_update_event():
    events = EventList()
    events.create_event(1, "Пожар", 5)
    events.update_event(1, "Наводнение", 3)
    assert events.events[1].event_type == "Наводнение"
    assert events.events[1].danger_level == 3


def test_create_notification():
    notifications = NotificationList()
    notifications.create_notification(1, "Не отправлено", "Очень опасно", "15.02.2025")
    assert 1 in notifications.notifications
    assert notifications.notifications[1].text == "Очень опасно"


def test_send_notification():
    notifications = NotificationList()
    notifications.create_notification(1, "Не отправлено", "Очень опасно", "15.02.2025")
    notifications.send_notification(1)
    assert notifications.notifications[1].status == "sent"


def test_update_notification_status():
    notifications = NotificationList()
    notifications.create_notification(1, "Не отправлено", "Очень опасно", "15.02.2025")
    notifications.update_notification_status(1, "delivered")
    assert notifications.notifications[1].status == "delivered"


def test_register_recipient():
    recipients = RecipientList()
    recipients.register_recipient(1, "Пермь", "12345")
    assert 1 in recipients.recipients
    assert recipients.recipients[1].location == "Пермь"


def test_update_recipient():
    recipients = RecipientList()
    recipients.register_recipient(1, "Пермь", "12345")
    recipients.update_recipient(1, "Москва", "67890")
    assert recipients.recipients[1].location == "Москва"
    assert recipients.recipients[1].contact == "67890"
