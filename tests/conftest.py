import pytest

from FSM_Generator.state import State
from FSM_Generator.event import Event
from FSM_Generator.fsm import FSM


@pytest.fixture
def states():
    """Fixture for a list of State objects."""
    return [State("Idle"), State("Active"), State("Stopped")]

@pytest.fixture
def events():
    """Fixture for a list of Event objects."""
    return [Event("start"), Event("stop"), Event("reset")]

@pytest.fixture
def fsm(states, events):
    """Fixture for a basic FSM instance with transitions for testing."""
    fsm_instance = FSM(states, events, states[0])
    s_idle, s_active, s_stopped = states
    e_start, e_stop, e_reset = events

    # Define a simple FSM behavior
    fsm_instance.add_transition(s_idle, e_start, s_active)
    fsm_instance.add_transition(s_active, e_stop, s_stopped)
    fsm_instance.add_transition(s_stopped, e_reset, s_idle)
    
    return fsm_instance

@pytest.fixture
def states_for_modThree():
    """Fixture for a list of State objects for modThree."""
    return [State("S0"), State("S1"), State("S2")]

@pytest.fixture
def events_for_modThree():
    """Fixture for a list of Event objects for modThree."""
    return [Event("e0"), Event("e1")]

@pytest.fixture
def fsm_modThree(states_for_modThree, events_for_modThree):
    """Fixture for a modThree FSM instance. 
       This is the example of ‘mod-three’ procedure"""
    fsm_instance = FSM(states_for_modThree, events_for_modThree, states_for_modThree[0])
    s0, s1, s2 = states_for_modThree
    e0, e1 = events_for_modThree

    # Define transitions for modThree FSM
    fsm_instance.add_transition(s0, e0, s0)
    fsm_instance.add_transition(s0, e1, s1)
    fsm_instance.add_transition(s1, e0, s2)
    fsm_instance.add_transition(s1, e1, s0)
    fsm_instance.add_transition(s2, e0, s1)
    fsm_instance.add_transition(s2, e1, s2)

    return fsm_instance