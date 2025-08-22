from FSM_Generator.event import Event

class ModThreeEvent(Event):
    """Represents an event in a ModThreeFSM class.

    A ModThreeEvent can only be initialized with a name that is '0', '1',
    corresponding to the possible inpus from a binary string.

    Attributes:
        name (str): The name of the event, which must be '0' or '1'.
    """
    def __init__(self, name):
        """Initializes a ModThreeEvent.

        Args:
            name (str): The name of the event.

        Raises:
            ValueError: If the provided name is not '0' or '1'.
        """
        if name not in ["0", "1"]:
            raise ValueError("Invalid event, a Mod Three Event must be '0' or '1'.")
        super().__init__(name)