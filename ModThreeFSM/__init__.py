"""A package containing a finite state machine (FSM) for calculating a binary number's remainder when divided by 3.

This package provides the core components for the Modulo 3 FSM:
- ModThreeEvent: Represents the binary digits '0' and '1' as events.
- ModThreeState: Represents the FSM's states, corresponding to remainders '0', '1', or '2'.
- ModThreeFSM: The main class that implements the FSM logic and handles the calculation.
"""
from ModThreeFSM.ModThreeEvent import ModThreeEvent
from ModThreeFSM.ModThreeState import ModThreeState
from ModThreeFSM.ModThreeFSM import ModThreeFSM