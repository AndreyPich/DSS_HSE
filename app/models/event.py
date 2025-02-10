#Модель ЧС
class Event:
    def __init__(self, event_id, event_type, danger_level, location):
        self.event_id = event_id
        self.event_type = event_type
        self.danger_level = danger_level
        self.location = location

    def __repr__(self):
        return (f"ID: {self.event_id}, Тип: {self.event_type}, "
                f"Уровень опасности: {self.danger_level}, Местоположение: {self.location or 'Не указано'}")
