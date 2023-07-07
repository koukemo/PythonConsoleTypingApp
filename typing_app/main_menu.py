from game_mode import GameMode
from util.standard_input_reader import StandardInputreader
from util.standard_csv_operator import StandardCsvOperator
import time
import random

class MainMenu:
    def display_mode(self) -> None:
        """Display game modes that can be selected.
        """
        print("Please select a difficulty.(1-3)")
        print("1: Easy")
        print("2: Normal")
        print("3: hard")

    def select_game_mode(self) -> GameMode:
        """Select the difficulty level of the game.

        Yields:
            GameMode: EASY, NORMAL, HARD defined in enum.
        """
        input_num = StandardInputreader.input_int()

        if input_num == 1:
            return GameMode.EASY
        elif input_num == 2:
            return GameMode.NORMAL
        elif input_num == 3:
            return GameMode.HARD
        else:
            print("Start Normal mode.")
            return GameMode.NORMAL
            
    def start_count_down(self, count_time: int) -> None:
        """Displays a countdown for a specified number of seconds.

        Args:
            count_time (int): Number of seconds to count down.
        """
        limit_time = count_time
        
        while limit_time > 0:
            print(f"{limit_time}..........")
            time.sleep(1)
            limit_time -= 1

    def start_game(self, game_mode: GameMode) -> int:
        """Start the game.

        Args:
            game_mode (GameMode): Selected game difficulty level.

        Yields:
            int: Elapsed time at the end of the game. [milliseconds]
        """
        question_count = 0
        
        question_list = []

        easy_list = StandardCsvOperator.convert_question_csv_to_list("easy")
        normal_list = StandardCsvOperator.convert_question_csv_to_list("normal")
        hard_list = StandardCsvOperator.convert_question_csv_to_list("hard")

        timer_start = time.time()

        if game_mode == GameMode.EASY:
            question_count = 5
            question_list.extend(easy_list)
        elif game_mode == GameMode.NORMAL:
            question_count = 10
            question_list.extend(easy_list)
            question_list.extend(normal_list)
        elif game_mode == GameMode.HARD:
            question_count = 20
            question_list.extend(easy_list)
            question_list.extend(normal_list)
            question_list.extend(hard_list)
        else:
            print("Ocuuring error")

        for question in random.sample(question_list, question_count):
            while True:
                answer = StandardInputreader.input_string(f"{question}: ")

                if question == answer:
                    print("OK!")
                    break
                else:
                    print("MISS...")

        timer_end = time.time()
        result_time = int((timer_end - timer_start) * 1000)
        print(f"Finished. time = {result_time}[ms]")

        return result_time

    def is_continue_game(self) -> None:
        print("Continue? (1: Yes / 2: No)")

        select_number = StandardInputreader.input_int()

        if select_number == 1:
            return
        elif select_number == 2:
            print("Quit the typing application.")
            exit(0)
        else:
            print("Please input correct number.")