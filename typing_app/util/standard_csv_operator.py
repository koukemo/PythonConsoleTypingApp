import sys
import os
import csv
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from game_mode import GameMode

class StandardCsvOperator:
    @staticmethod
    def convert_question_csv_to_list(csv_file_name: str) -> list[str]:
        """Convert the question CSV to list data.

        Args:
            csv_file_name (str): CSV file with question data.

        Yeilds:
            list[str]: Converted question list data.
        """
        current_dir = os.getcwd()
        resource_dir = 'typing_app/resources'
        target_file_dir = os.path.join(current_dir, resource_dir)
        target_file_path = os.path.join(target_file_dir, csv_file_name + ".csv")

        with open(target_file_path, encoding='utf8', newline='') as f:
            csv_reader = csv.reader(f)
            results = [row[0] for row in csv_reader]

        return results
    
    @staticmethod
    def convert_ranking_csv_to_list(csv_file_name: str) -> tuple[list[int], list[GameMode], list[int]]:
        """Convert the ranking CSV to list data.

        Args:
            csv_file_name (str): CSV file with ranking data.
        
        Yeilds:
            tuple[list[int], list[GameMode], list[int]]: A tuple of time list data, game mode list data, and score list data.
        """
        current_dir = os.getcwd()
        resource_dir = 'typing_app/resources'
        target_file_dir = os.path.join(current_dir, resource_dir)
        target_file_path = os.path.join(target_file_dir, csv_file_name + ".csv")

        with open(target_file_path, encoding='utf8', newline='') as f:
            csv_reader = csv.reader(f)
            time_list = [int(row[0]) for row in csv_reader]
            game_mode_list = [GameMode(row[1]) for row in csv_reader]
            score_list = [int(row[2]) for row in csv_reader]

        return time_list, game_mode_list, score_list
    
    @staticmethod
    def convert_ranking_list_to_csv(time_list: list[int], game_mode_list: list[GameMode], score_list: list[int], csv_file_name: str) -> bool:
        """Convert the ranking list to CSV data.

        Args:
            time_list (list[int]): List of times to be registered in CSV.
            game_mode_list (list[GameMode]): List of game modes to be registered in CSV.
            score_list (list[int]): List of scores to be registered in CSV.

        Yeilds:
            bool: True -> CSV could be created., False -> Could not create CSV.
        """
        is_created = False
        
        current_dir = os.getcwd()
        resource_dir = 'typing_app/resources'
        target_file_dir = os.path.join(current_dir, resource_dir)
        target_file_path = os.path.join(target_file_dir, csv_file_name + ".csv")

        with open(target_file_path, 'w', newline="") as f:
            is_created = True
            writer = csv.writer(f)
            for time, game_mode, score in zip(time_list, game_mode_list, score_list):
                writer.writerow([time, game_mode.value, score])

        return is_created