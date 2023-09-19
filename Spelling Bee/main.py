"""
Author: Brendan Cook
Date Updated: 09/18/23
Runs the application.
"""


from FrontEnd.UI import User_Interface
from BackEnd.search import SearchWords
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)


if __name__ == '__main__':
    print(Style.BRIGHT + Fore.BLUE + "Enter the letters for the puzzle you would like to complete.")
    print(Style.BRIGHT + Fore.BLUE + "Enter 'Exit' to leave")
    while True:
        ui = User_Interface()
        search = SearchWords()

        if ui.user_input() is False:
            print(Style.BRIGHT + Fore.BLUE + "Goodbye")
            break

        search.search(ui.get_all_letters())
        ui.show_results(search.get_results())

        if ui.cont_puzzle() is False:
            print(Style.BRIGHT + Fore.BLUE + "Goodbye")
            break
