from FSM_Generator.state import State

class ModThreeState(State):
    """Represents a state in a ModThreeFSM class.

    A ModThreeState can only be initialized with a name that is '0', '1', or '2',
    corresponding to the possible remainders when a number is divided by 3.

    Attributes:
        name (str): The name of the state, which must be '0', '1', or '2'.
    """
    def __init__(self, name):
        """Initializes a ModThreeState.

        Args:
            name (str): The name of the state.

        Raises:
            ValueError: If the provided name is not '0', '1', or '2'.
        """
        if name not in ["0", "1", "2"]:
            raise ValueError("Invalid state, a Mod Three State must be '0', '1', '2'.")
        super().__init__(name)