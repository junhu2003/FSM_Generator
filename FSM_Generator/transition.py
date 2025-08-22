from FSM_Generator.state import State
from FSM_Generator.event import Event

class Transition:
    """Represents a transition from a start state to a next state triggered by an event."""
    def __init__(self, start_state: State, event: Event, next_state: State):
        if not isinstance(start_state, State):
            raise TypeError("start_state must be an instance of State.")
        if not isinstance(event, Event):
            raise TypeError("event must be an instance of Event.")
        if not isinstance(next_state, State):
            raise TypeError("next_state must be an instance of State.")        

        self.start_state = start_state
        self.event = event
        self.next_state = next_state        

    def __repr__(self):
        return f"Transition({self.start_state.name} --{self.event.name}--> {self.next_state.name})"