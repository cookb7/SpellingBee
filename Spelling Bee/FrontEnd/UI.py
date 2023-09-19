"""
Author: Brendan Cook
Date Updated: 09/18/23
Defines classes for simple UI.
"""

from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)


class User_Interface():
    """Defines functions for user input and output"""
    def __init__(self) -> None:
        """
        Initializes the user interface. Creates the variables
        for the letters used in the puzzle.
        """
        self._primary_letter = None
        self._secondary_letters = []
    
    def user_input(self):
        """
        Gets user input for the letters used in the puzzle.
        Calls two private functions for user input the letters.
        """
        while True:
            self._input_primary()
            if self._primary_letter.lower() == 'exit':
                return False
            if len(self._primary_letter) == 0:
                print(Fore.RED + "You must input a letter. Please try again")
            elif len(self._primary_letter) > 1:
                print(Fore.RED + "Only one letter can be input. Please try again.")
            else:
                break

        while True:
            self._input_secondary()
            if self._secondary_letters[0].lower() == 'exit':
                return False
            if len(self._secondary_letters) < 6:
                print(Fore.RED + "You must input six letters. Please try again.")
            elif len(self._secondary_letters) > 6:
                print(Fore.RED + "You can only input six letters. Please try again.")
            else:
                break

    def _input_primary(self):
        """Receives user input for the primary letter in the puzzle."""
        self._primary_letter = input("Please enter the primary letter: ")

    def _input_secondary(self):
        """Receives user input fot the secondary letters in the puzzle."""
        letters = input("Please enter the six secondary numbers with a space between each: ")
        self._secondary_letters = letters.split()
    
    def get_all_letters(self):
        """Getter function to return all the letters in the puzzle."""
        letters = self._secondary_letters
        letters.append(self._primary_letter)
        return letters
    
    def show_results(self, results):
        """
        Prints all the possible words for the puzzle.
        Prints 10 words per row. Takes a list of words as an 
        argument.
        """
        self._alphabetize(results)
        print(Fore.GREEN + 'Results:')
        for i in range(0, len(results), 10):
            group = ' '.join(map(str, results[i: i + 10]))
            print(Fore.GREEN + group)

    def _alphabetize(self, results):
        """Alphabetizes the results."""
        results.sort()

    def cont_puzzle(self):
        """
        Receives user input if they would like to
        start over with new letters.
        """
        print(Style.BRIGHT + Fore.BLUE + 
            "Would you like to enter new letters for a different puzzle? Yes or No:")
        new_puzzle = input()
        if new_puzzle.lower() == 'yes':
            return True
        else:
            return False
        