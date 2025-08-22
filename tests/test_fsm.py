import pytest

from FSM_Generator.state import State
from FSM_Generator.event import Event
from FSM_Generator.fsm import FSM

# Re-use previous tests for other classes
# ... (all previous tests for State, Event, Transition, and FSM init remain valid) ...

def test_fsm_initialization_with_initial_state(states, events):
    """Test FSM initialization with a valid initial state."""
    s_idle, s_active, _ = states
    
    fsm = FSM(states, events, s_idle)
    assert fsm.current_state == s_idle

def test_fsm_initialization_with_invalid_initial_state(states, events):
    """Test FSM initialization with an initial state not in the states list."""
    invalid_state = State("S_invalid")
    
    with pytest.raises(ValueError, match="initial_state must be a valid State object"):
        FSM(states, events, invalid_state)

def test_fsm_process_successful_transition(fsm, states, events):
    """Test a successful state transition."""
    s_idle, s_active, s_stopped = states
    e_start, e_stop, _ = events
    
    # Check initial state
    assert fsm.current_state == s_idle
    
    # Process 'start' event
    transition_occurred = fsm.process(e_start)
    assert transition_occurred
    assert fsm.current_state == s_active
    
    # Process 'stop' event
    transition_occurred = fsm.process(e_stop)
    assert transition_occurred
    assert fsm.current_state == s_stopped

def test_fsm_process_no_transition(fsm, states, events):
    """Test processing an event for which no transition is defined."""
    s_idle, s_active, _ = states
    _, e_stop, _ = events
    
    # FSM starts in 'Idle'
    assert fsm.current_state == s_idle
    
    # Try to process 'start' from 'Idle' - no transition defined
    transition_occurred = fsm.process(e_stop)
    assert not transition_occurred
    assert fsm.current_state == s_idle # State should not change

def test_fsm_process_with_invalid_event(fsm):
    """Test processing an event that is not part of the FSM's event set."""
    invalid_event = Event("invalid_event")
    
    with pytest.raises(ValueError, match="is not a valid event for this FSM."):
        fsm.process(invalid_event)

def test_fsm_process_transition_action(fsm, states, events):
    """Test that the action function is executed during a transition."""
    s_idle, s_active, _ = states
    e_start, _, _ = events
    
    # Add a transition with an action
    fsm.add_transition(s_idle, e_start, s_active)
    
    fsm.process(e_start)    
    assert fsm.current_state == s_active