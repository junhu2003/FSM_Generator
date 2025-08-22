# A simple, generic Finite State Machine (FSM) implementation in Python.

This package provides a modular and extensible framework for building state machines.
It includes core components such as:
- **State**: Represents a single, distinct state.
- **Event**: Represents an action or trigger that causes a state transition.
- **Transition**: Defines a rule for moving from one state to another based on an event.
- **FSM**: The main class that manages states, events, and transitions, allowing for event processing and state changes.

Key features include:
- Clear separation of concerns with dedicated classes for each component.
- Parameter validation to ensure correct usage.
- A `check_coverage` method to verify that all state-event combinations have defined transitions.
- A protected `_current_state` and a `process` method to manage and execute state transitions securely.
