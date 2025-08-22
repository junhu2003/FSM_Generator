class Event:
    """Represents an event that triggers a transition in the FSM."""
    def __init__(self, name: str):
        if not isinstance(name, str) or not name:
            raise ValueError("Event name must be a non-empty string.")
        self.name = name

    def __eq__(self, other):
        return isinstance(other, Event) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f"Event('{self.name}')"