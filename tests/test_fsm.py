import pytest

from FSM_Generator.state import State
from FSM_Generator.event import Event
from FSM_Generator.transition import Transition
from FSM_Generator.fsm import FSM

# Re-use previous tests for other classes
# ... (all previous tests for State, Event, Transition, and FSM init remain valid) ...

def test_state_initialization_with_invalid_parameter():
    """Test state initialization with invalid parameter"""
    with pytest.raises(ValueError, match="State name must be a non-empty string."):
        State(1)

    with pytest.raises(ValueError, match="State name must be a non-empty string."):
        State(True)

def test_state_object_methods():
    """test state object methods"""
    s_state_1 = State("test_state")
    s_state_2 = State("test_state")

    assert s_state_1 == s_state_2    

def test_event_initialization_with_invalid_parameter():
    """Test Event initialization with invalid parameter"""
    with pytest.raises(ValueError, match="Event name must be a non-empty string."):
        Event(1)

    with pytest.raises(ValueError, match="Event name must be a non-empty string."):
        Event(False)

def test_event_object_methods():
    """test event object methods"""
    s_event_1 = Event("test_event")
    s_event_2 = Event("test_event")

    assert s_event_1 == s_event_2    

def test_transition_initialization_with_invalid_parameter():
    """Test transition initialization with invalid parameter"""
    with pytest.raises(TypeError, match="start_state must be an instance of State."):
        Transition("Active", Event("Start"), State("Stop"))

    with pytest.raises(TypeError, match="event must be an instance of Event."):
        Transition(State("Active"), "Start", State("Stop"))

    with pytest.raises(TypeError, match="next_state must be an instance of State."):
        Transition(State("Active"), Event("Start"), "Stop")
    

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

def test_fsm_add_transition_unsuccessful(fsm, states, events):
    """test fsm add transition unsuccessful"""    
    with pytest.raises(ValueError, match="not a valid state for this FSM."):
        fsm.add_transition(State("invalid_state"), events[0], states[1])

    with pytest.raises(ValueError, match="not a valid event for this FSM."):
        fsm.add_transition(states[0], Event("invalid_event"), states[1])

    with pytest.raises(ValueError, match="not a valid state for this FSM."):
        fsm.add_transition(states[1], events[0], State("invalid_state"))

def test_fsm_add_transition_successful(states, events):
    """test fsm add transition successful"""    
    fsm = FSM(states, events, states[0])
    fsm.add_transition(states[2], events[0], states[1])
    assert states[2] in fsm.get_transitions()

def test_fsm_check_coverage_or_not(states, events):
    """test_fsm_check_coverage_or_not"""    
    fsm_not_fully_covered = FSM(states, events, states[0])
    fsm_not_fully_covered.add_transition(states[0], events[0], states[1])
    fsm_not_fully_covered.add_transition(states[0], events[1], states[1])
    fsm_not_fully_covered.add_transition(states[0], events[2], states[1])
    is_fully_covered, missing_combinations = fsm_not_fully_covered.check_coverage()
    assert not is_fully_covered
    assert len(missing_combinations) > 0
    
    fsm_fully_covered = FSM(states, events, states[0])
    fsm_fully_covered.add_transition(states[0], events[0], states[1])
    fsm_fully_covered.add_transition(states[0], events[1], states[1])
    fsm_fully_covered.add_transition(states[0], events[2], states[1])
    fsm_fully_covered.add_transition(states[1], events[0], states[1])
    fsm_fully_covered.add_transition(states[1], events[1], states[1])
    fsm_fully_covered.add_transition(states[1], events[2], states[1])
    fsm_fully_covered.add_transition(states[2], events[0], states[1])
    fsm_fully_covered.add_transition(states[2], events[1], states[1])
    fsm_fully_covered.add_transition(states[2], events[2], states[1])
    is_fully_covered, missing_combinations = fsm_fully_covered.check_coverage()
    assert is_fully_covered
    assert len(missing_combinations) == 0

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