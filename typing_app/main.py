from main_menu import MainMenu
from ranking_menu import RankingMenu
from ranking import Ranking

def main():
    """main function
    """
    main_menu = MainMenu()
    ranking_menu = RankingMenu()

    ranking_menu.create_ranking_list()

    while True:
        main_menu.display_mode()
        select_mode = main_menu.select_game_mode()
        main_menu.start_count_down(5)

        result_time = main_menu.start_game(select_mode)
        ranking = Ranking(result_time, select_mode)

        ranking_menu.register_ranking(ranking)

        ranking_menu.display_ranking_list()
        ranking_menu.create_ranking_csv()
        main_menu.is_continue_game()

if __name__ == "__main__":
    main()