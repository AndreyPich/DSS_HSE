from app.entities.eventList import EventList
from app.entities.notificationList import NotificationList
from app.entities.recipientList import RecipientList


def start():
    events = EventList()
    notifications = NotificationList()
    recipients = RecipientList()
    notifications.create_notification(1, "Не отправлено", "Очень опасно", "15.02.2025")
    notifications.create_notification(2, "Отправлено", "Опасно", "25.02.2025")
    notifications.create_notification(3, "Отправлено", "Предупреждение", "05.02.2025")
    recipients.register_recipient(1, "Пермь", "12345")
    recipients.register_recipient(2, "Березники", "12346")
    recipients.register_recipient(3, "Кунгур", "12347")

    while True:
        print("\nВыберите команду:")
        print("1. Создать чрезвычайное событие")
        print("2. Обновить информацию о ЧС")
        print("3. Назначить местоположение ЧС")
        print("4. Вывести все события ЧС")
        print("5. Вывести все уведомления")
        print("6. Вывести всех получаетелей")
        print("10. Выход")

        command = input("Введите номер команды: ")

        if command == "1":
            event_id = int(input("Введите ID события: "))
            event_type = input("Введите тип: ")
            danger_level = int(input("Введите уровень опасности (1-5): "))
            events.create_event(event_id, event_type, danger_level)
            print("Событие создано.")

        elif command == "2":
            event_id = int(input("Введите ID события: "))
            event_type = input("Введите новый тип события: ")
            danger_level = input("Введите новый уровень опасности: ")
            events.update_event(event_id, event_type or None, int(danger_level) if danger_level else None)
            print("Событие обновлено.")

        elif command == "3":
            event_id = int(input("Введите ID события: "))
            location = input("Введите местоположение: ")
            events.assign_location(event_id, location)
            print("Местоположение обновлено.")

        elif command == "4":
            events.list_events()

        elif command == "5":
            notifications.list_notifications()

        elif command == "6":
            recipients.list_recipients()

        elif command == "10":
            print("Выход из программы.")
            sys.exit()

        else:
            print("Неверный ввод, попробуйте снова.")
