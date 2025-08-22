import pytest

from FSM_Generator.state import State
from FSM_Generator.event import Event
from FSM_Generator.fsm import FSM
from tests.conftest import fsm_modThree_not_fully_trained

# Re-use previous tests for other classes
# ... (all previous tests for State, Event, Transition, and FSM init remain valid) ...

def test_fsm_modThree_not_fully_trained(fsm_modThree_not_fully_trained):
    """Test A NOT FULLY TRAINED FSM Object."""
    fsm = fsm_modThree_not_fully_trained
        
    is_fully_trained, missing_combinations = fsm.check_coverage()
    assert is_fully_trained == False
    assert len(missing_combinations) > 0

def test_fsm_modThree_calculate_1010_mod_by_three(fsm_modThree_fully_trained):
    """Test mode Three FSM calculating 0x1010 mod by three."""
    fsm = fsm_modThree_fully_trained

    is_fully_trained, missing_combinations = fsm.check_coverage()
    assert is_fully_trained == True
    assert len(missing_combinations) == 0

    binary_input = [1, 0, 1, 0]    
    for event in [Event("e" + str(e)) for e in binary_input]:
        fsm.process(event)
 
    assert fsm.current_state.name == "S1"

def test_fsm_modThree_calculate_1111_mod_by_three(fsm_modThree_fully_trained):
    """Test mode Three FSM calculating 0x1111 mod by three."""
    fsm = fsm_modThree_fully_trained

    binary_input = [1, 1, 1, 1]    
    for event in [Event("e" + str(e)) for e in binary_input]:
        fsm.process(event)
 
    assert fsm.current_state.name == "S0"        

