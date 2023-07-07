"""
The game_mode module provides the GameMode Enum class for managing the main menu of the typing app.
"""
from enum import Enum

class GameMode(Enum):
    """
    GameMode Enum class
    """
    EASY = "EASY"
    NORMAL = "NORMAL"
    HARD = "HARD"