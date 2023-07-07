from game_mode import GameMode

"""
The ranking module provides the Ranking class for managing rankings in the typing app.
"""
class Ranking:
    """
    Ranking class
    """
    def __init__(self, time: int, game_mode: GameMode):
        """Initialization of Ranking class.
        
        Args:
            game_mode (GameMode): EASY, NORMAL, HARD defined in enum.
        """
        self._time = time
        self._game_mode = game_mode
        self._score = self.calculate_score()

    @property
    def time(self):
        """int: Time on ranking.
        """
        return self._time
    
    @property
    def game_mode(self):
        """gameMode: Game mode on the ranking.
        """
        return self._game_mode
    
    @property
    def score(self):
        """int: Score on ranking.
        """
        return self._score
    
    def calculate_score(self) -> int:
        """Calculate the score.

        Yeilds:
            int: Calculated score (max: 10000)
        """
        MAX_SCORE = 10000

        mode_score_magnification = 0
        if self._game_mode == GameMode.EASY:
            mode_score_magnification = 0.75
        elif self._game_mode == GameMode.NORMAL:
            mode_score_magnification = 0.9
        elif self._game_mode == GameMode.HARD:
            mode_score_magnification = 1

        result_score = int(mode_score_magnification * (MAX_SCORE - (self._time / 100)))

        if result_score < 0:
            result_score = 0

        return result_score