import pytest

from FSM_Generator.state import State
from FSM_Generator.event import Event
from FSM_Generator.fsm import FSM

# Re-use previous tests for other classes
# ... (all previous tests for State, Event, Transition, and FSM init remain valid) ...

def test_fsm_modThree_calculate_110_mod_by_three(fsm_modThree):
    """Test mode Three FSM calculating 0b110 mod by three."""
    fsm = fsm_modThree

    is_fully_trained, missing_combinations = fsm.check_coverage()
    assert is_fully_trained == True
    assert len(missing_combinations) == 0

    binary_input = [1, 1, 0]    
    for event in [Event("e" + str(e)) for e in binary_input]:
        fsm.process(event)
 
    assert fsm.current_state.name == "S0"


def test_fsm_modThree_calculate_1010_mod_by_three(fsm_modThree):
    """Test mode Three FSM calculating 0b1010 mod by three."""
    fsm = fsm_modThree

    is_fully_trained, missing_combinations = fsm.check_coverage()
    assert is_fully_trained == True
    assert len(missing_combinations) == 0

    binary_input = [1, 0, 1, 0]    
    for event in [Event("e" + str(e)) for e in binary_input]:
        fsm.process(event)
 
    assert fsm.current_state.name == "S1"

def test_fsm_modThree_calculate_1111_mod_by_three(fsm_modThree):
    """Test mode Three FSM calculating 0b1111 mod by three."""
    fsm = fsm_modThree

    binary_input = [1, 1, 1, 1]    
    for event in [Event("e" + str(e)) for e in binary_input]:
        fsm.process(event)
 
    assert fsm.current_state.name == "S0"        

def test_fsm_modThree_calculate_1110_mod_by_three(fsm_modThree):
    """Test mode Three FSM calculating 0b1111 mod by three."""
    fsm = fsm_modThree

    binary_input = [1, 1, 1, 0]    
    for event in [Event("e" + str(e)) for e in binary_input]:
        fsm.process(event)
 
    assert fsm.current_state.name == "S2"