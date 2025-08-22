from FSM_Generator.state import State
from FSM_Generator.event import Event
from FSM_Generator.transition import Transition

class FSM:
    """
    Represents a generic Finite State Machine.

    The FSM is defined by a set of states, a set of events, and a collection
    of transitions. It includes a current state and a method to process events.
    """
    def __init__(self, states: list, events: list, initial_state: State):
        """
        Initializes the FSM with states, events, and an initial state.

        Args:
            states (list): A list of State objects.
            events (list): A list of Event objects.
            initial_state (State): The starting state of the FSM.
        
        Raises:
            ValueError: If states or events lists are empty, contain invalid types,
                        or if the initial_state is not in the list of states.
        """
        if not states or not all(isinstance(s, State) for s in states):
            raise ValueError("states must be a non-empty list of State objects.")
        if not events or not all(isinstance(e, Event) for e in events):
            raise ValueError("events must be a non-empty list of Event objects.")
        if not isinstance(initial_state, State) or initial_state not in states:
            raise ValueError("initial_state must be a valid State object within the provided states.")

        self._states = set(states)
        self._events = set(events)
        self._transitions = {}
        self._current_state = initial_state

    @property
    def current_state(self) -> State:
        """Returns the current state of the FSM."""
        return self._current_state

    def add_transition(self, start_state: State, event: Event, next_state: State):
        """Adds a transition to the FSM."""
        if start_state not in self._states:            
            raise ValueError(f"Start state {start_state} is not a valid state for this FSM.")
        if event not in self._events:
            raise ValueError(f"Event {event} is not a valid event for this FSM.")
        if next_state not in self._states:
            raise ValueError(f"Next state {next_state} is not a valid state for this FSM.")

        if start_state not in self._transitions:
            self._transitions[start_state] = {}
        
        self._transitions[start_state][event] = Transition(start_state, event, next_state)

    def process(self, event: Event):
        """
        Processes an event, triggering a state transition if a valid one exists.

        Args:
            event (Event): The event to process.
        
        Returns:
            bool: True if a transition occurred, False otherwise.
        
        Raises:
            ValueError: If the event is not valid for this FSM.
        """
        if event not in self._events:
            raise ValueError(f"Event {event} is not a valid event for this FSM.")
        
        try:
            transition = self._transitions[self._current_state][event]

            # Update the current state
            self._current_state = transition.next_state
            return True
        except KeyError:
            # No transition defined for the current state and event
            return False

    def check_coverage(self):
        """
        Checks if every possible state and event combination has a defined transition.
        """
        missing_transitions = []
        for state in self._states:
            for event in self._events:
                if state not in self._transitions or event not in self._transitions[state]:
                    missing_transitions.append((state, event))
        
        return len(missing_transitions) == 0, missing_transitions

    def get_states(self) -> set:
        """Returns a set of the FSM's states."""
        return self._states

    def get_events(self) -> set:
        """Returns a set of the FSM's events."""
        return self._events

    def get_transitions(self) -> dict:
        """Returns a copy of the FSM's transitions dictionary."""
        return self._transitions.copy()