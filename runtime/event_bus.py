from collections import defaultdict


class EventBus:

    def __init__(self):
        self.listeners = defaultdict(list)

    def subscribe(self, event_name, callback):
        self.listeners[event_name].append(callback)

    def publish(self, event_name, data=None):

        for callback in self.listeners[event_name]:
            callback(data)


event_bus = EventBus()