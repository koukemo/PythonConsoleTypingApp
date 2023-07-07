"""
The ranking_list module provides the RankingList class for managing rankings in the typing app.
"""
from game_mode import GameMode
from ranking import Ranking
from util.standard_csv_operator import StandardCsvOperator

class RankingList:
    """
    The RankingMenu class provides functionality for managing rankings.
    It allows registering, displaying, and creating ranking data lists.
    """
    def __init__(self):
        """Initialization of RankingList class.

        Note:
            Create an empty list with elements of type Ranking.
        """
        self._ranking_list: list[Ranking] = []

    @property
    def ranking_list(self):
        """list[Ranking]: Ranking type list.
        """
        return self._ranking_list
    
    def create_ranking_list(self, csv_file_name: str) -> None:
        """Create a ranking list.

        Create a ranking list from CSV.
        If no data exists in the CSV, create a ranking list 
        from predefined default values.

        Args:
            csv_file_name (str): CSV file with ranking data.
        """
        DEFAULT_RANKING_LIST_COUNT = 10
        
        time_list, game_mode_list, _ = StandardCsvOperator.convert_ranking_csv_to_list(csv_file_name)
        ranking_list_count = len(time_list)


        if ranking_list_count == DEFAULT_RANKING_LIST_COUNT:
            for index in range(ranking_list_count):
                ranking = Ranking(time_list[index], game_mode_list[index])
                self._ranking_list.append(ranking)
        else:
            default_time_list = [999999999999999] * DEFAULT_RANKING_LIST_COUNT
            default_game_mode_list = [GameMode.NORMAL] * DEFAULT_RANKING_LIST_COUNT

            for index in range(DEFAULT_RANKING_LIST_COUNT):
                default_ranking = Ranking(default_time_list[index], default_game_mode_list[index])
                self._ranking_list.append(default_ranking)

    def update_ranking_list(self, ranking: Ranking) -> None:
        """ Update a ranking list.

        Compare the existing ranking data list 
        with the new ranking data and update the ranking.
        
        Args:
            ranking (Ranking): Candidate ranking data for update.
        """
        fluctating_index = 0
        is_update = False

        for old_ranking in self._ranking_list:
            if ranking.time < old_ranking.time:
                is_update = True
                break

            fluctating_index += 1

        if is_update:
            self._ranking_list.insert(fluctating_index, ranking)
            self._ranking_list = self._ranking_list[:-1]

    def print_ranking_list(self) -> None:
        """Print elements of the ranking data list.
        """
        index = 1

        print('{:>4}  {:>15} {:>8} {:>5}'.format("Rank", "Time", "GameMode", "Score"))
        print("------------------------------------")
        for ranking in self._ranking_list:
            print('{:>4}  {:>15} {:>8} {:>5}'.format(index, ranking.time, ranking.game_mode.value, ranking.score))
            index += 1

    def create_ranking_csv(self, csv_file_name: str) -> bool:
        """Create a ranking CSV.

        Args:
            csv_file_name (str): CSV file with ranking data.

        Yeilds:
            bool: True -> CSV could be created., False -> Could not create CSV.
        """
        time_list: list[int] = []
        game_mode_list: list[GameMode] = []
        score_list: list[int] = []
        
        for ranking in self._ranking_list:
            time_list.append(ranking.time)
            game_mode_list.append(ranking.game_mode)
            score_list.append(ranking.score)

        is_created = StandardCsvOperator.convert_ranking_list_to_csv(time_list, game_mode_list, score_list, csv_file_name)

        return is_created