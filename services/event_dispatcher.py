from src.interfaces.event_listener import EventListener


class EventDispatcher:
    def __init__(self):
        self._listeners: list[EventListener] = []

    def attach(self, event_listener: EventListener):
        self._listeners.append(event_listener)

    def detach(self, event_listener: EventListener):
        self._listeners.remove(event_listener)

    def notify(self, event_data):
        for listener in self._listeners:
            listener.update(event_data)

