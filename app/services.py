# Сервисы для обработки команд
events_db = {}
notifications_db = {}
recipients_db = {}

def handle_create_event(command):
    event = command.event
    events_db[event['event_id']] = event
    return f"Event {event['event_id']} created."

def handle_update_event(command):
    event = events_db.get(command.event_id)
    if event:
        event.update(command.updated_data)
        return f"Event {command.event_id} updated."
    return "Event not found."

def handle_location_to_event(command):
    event = events_db.get(command.event_id)
    if event:
        event['location'] = command.location
        return f"Event {command.event_id} location updated."
    return "Event not found."

def handle_channel_to_event(command):
    event = events_db.get(command.event_id)
    if event:
        event['channel'] = command.channel
        return f"Event {command.event_id} channel updated."
    return "Event not found."

def handle_create_notification(command):
    notification = command.notification
    notifications_db[notification['notification_id']] = notification
    return f"Notification {notification['notification_id']} created."

def handle_send_notification(command):
    notification = notifications_db.get(command.notification_id)
    if notification:
        return f"Notification {command.notification_id} sent to recipient {command.recipient_id}."
    return "Notification not found."

def handle_update_notification_status(command):
    notification = notifications_db.get(command.notification_id)
    if notification:
        notification['status'] = command.status
        return f"Notification {command.notification_id} status updated to {command.status}."
    return "Notification not found."

def handle_register_recipient(command):
    recipient = command.recipient
    recipients_db[recipient['recipient_id']] = recipient
    return f"Recipient {recipient['recipient_id']} registered."

def handle_update_recipient(command):
    recipient = recipients_db.get(command.recipient_id)
    if recipient:
        recipient.update(command.updated_data)
        return f"Recipient {command.recipient_id} updated."
    return "Recipient not found."
