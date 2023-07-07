"""
The ranking_menu module provides the RankingMenu class for managing rankings in the typing app.
"""
from ranking_list import RankingList
from ranking import Ranking

class RankingMenu:
    """
    RankingMenu class
    """
    def __init__(self):
        """Initialization of RankingMenu class.

        Note:
            Create an instance of the RankingList type.
        """
        self._ranking_list = RankingList()

    def register_ranking(self, ranking: Ranking) -> None:
        """Update process to existing rankings.

        Args:
            ranking (Ranking): Ranking data to be updated.
        """
        self._ranking_list.update_ranking_list(ranking)

    def display_ranking_list(self) -> None:
        """Display elements of the ranking data list.
        """
        self._ranking_list.print_ranking_list()

    def create_ranking_list(self) -> RankingList:
        """Create a new ranking data list.
        
        Yeilds:
            RankingList: Ranking list created.
        """
        CSV_FILE_NAME = "ranking"
        self._ranking_list.create_ranking_list(CSV_FILE_NAME)

        return self._ranking_list
    
    def create_ranking_csv(self) -> bool:
        """Create a ranking CSV.

        Yeilds:
            bool: True -> CSV could be created., False -> Could not create CSV.
        """
        CSV_FILE_NAME = "ranking"
        is_created = self._ranking_list.create_ranking_csv(CSV_FILE_NAME)

        return is_created
