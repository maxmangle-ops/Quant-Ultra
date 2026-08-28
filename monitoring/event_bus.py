class EventBus:

    def __init__(self):

        self.listeners = {}

    def subscribe(

        self,

        event,

        callback,

    ):

        self.listeners.setdefault(

            event,

            []

        ).append(callback)

    def publish(

        self,

        event,

    ):

        listeners = self.listeners.get(

            event.event_type,

            []

        )

        for callback in listeners:

            callback(event)