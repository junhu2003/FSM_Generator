class State:
    """Represents a single state in a Finite State Machine."""
    def __init__(self, name: str):
        if not isinstance(name, str) or not name:
            raise ValueError("State name must be a non-empty string.")
        self.name = name

    def __eq__(self, other):
        return isinstance(other, State) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f"State('{self.name}')"