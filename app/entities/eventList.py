from app.models.event import Event


class EventList:
    def __init__(self):
        self.events = {}

    def create_event(self, event_id, event_type, danger_level):
        """Создание нового ЧС."""
        if event_id in self.events:
            raise ValueError("Событие с таким ID уже существует.")
        self.events[event_id] = Event(event_id, event_type, danger_level, None)

    def update_event(self, event_id, event_type=None, danger_level=None):
        """Обновление информации о ЧС."""
        if event_id not in self.events:
            raise ValueError("Событие не найдено.")
        event = self.events[event_id]
        if event_type:
            event.event_type = event_type
        if danger_level:
            event.danger_level = danger_level

    def assign_location(self, event_id, location=None):
        """Обновление информации о ЧС."""
        if event_id not in self.events:
            raise ValueError("Событие не найдено.")
        event = self.events[event_id]
        if location:
            event.location = location


    def list_events(self):
        """Вывода всех ЧС."""
        if not self.events:
            print("Нет зарегистрированных событий.")
        else:
            print("События:")
            for event in self.events.values():
                print(event)
