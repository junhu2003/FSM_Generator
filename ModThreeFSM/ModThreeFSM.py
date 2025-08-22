from FSM_Generator.fsm import FSM

from ModThreeFSM.ModThreeEvent import ModThreeEvent
from ModThreeFSM.ModThreeState import ModThreeState

class ModThreeFSM:
    """A finite state machine (FSM) to calculate the remainder of a binary number when divided by 3.

    This class uses a custom FSM implementation to determine the value of a binary number
    modulo 3. The states of the FSM represent the current remainder (0, 1, or 2), and
    each '0' or '1' in the binary string acts as an event that transitions the FSM to the
    next state.
    """
    def __init__(self):
        """Initializes the ModThreeFSM by defining its states, events, and transitions.

        The FSM is configured with three states ('0', '1', '2') and two events ('0', '1').
        Transitions are set up to mimic the logic of a modulo 3 calculation on a binary
        string.
        """
        states = [ModThreeState("0"), ModThreeState("1"), ModThreeState("2")]
        events = [ModThreeEvent("0"), ModThreeEvent("1")]
        initial_state = ModThreeState("0")
        self.fsm_processor = FSM(states, events, initial_state)

        # Transition for state 0
        self.fsm_processor.add_transition(ModThreeState("0"), ModThreeEvent("0"), ModThreeState("0"))
        self.fsm_processor.add_transition(ModThreeState("0"), ModThreeEvent("1"), ModThreeState("1"))
        # Transition for state 1
        self.fsm_processor.add_transition(ModThreeState("1"), ModThreeEvent("0"), ModThreeState("2"))
        self.fsm_processor.add_transition(ModThreeState("1"), ModThreeEvent("1"), ModThreeState("0"))
        # Transition for state 2
        self.fsm_processor.add_transition(ModThreeState("2"), ModThreeEvent("0"), ModThreeState("1"))
        self.fsm_processor.add_transition(ModThreeState("2"), ModThreeEvent("1"), ModThreeState("2"))

    def is_binary_string(self, s: str) -> bool:
        """Checks if a given string is a valid binary number string.

        Args:
            s (str): The string to be checked.

        Returns:
            bool: True if the string contains only '0's and '1's, False otherwise.
        """
        return set(s).issubset({"0", "1"})
    
    def mod_by_three(self, binary_num_str: str) -> int:
        """Calculates the remainder of a binary number string when divided by 3.

        The method processes the input string digit by digit, updating the FSM's state
        based on the transitions. The final state of the FSM represents the remainder.

        Args:
            binary_num_str (str): The binary number string.

        Returns:
            int: The remainder of the binary number divided by 3.

        Raises:
            ValueError: If the input string is not a valid binary number.
        """
        if not self.is_binary_string(binary_num_str):
            raise ValueError("Invalid binary number string.")
        
        for event_str in binary_num_str:
            self.fsm_processor.process(ModThreeEvent(event_str))

        return int(self.fsm_processor.current_state.name)
