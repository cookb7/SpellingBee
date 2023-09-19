"""
Author: Brendan Cook
Date Updated: 09/18/23
Defines a class for searching the words dictionary.
"""


import json


class SearchWords():
    def __init__(self) -> None:
        """
        Initialize backend functions for puzzle.
        Loads JSON file with possible words for puzzle.
        """
        with open('./BackEnd/words_dictionary.json', 'r') as file:
            words = json.load(file)
            self._words = words.keys()
        self._results = []

    def search(self, letters):
        """
        Searches the JSON dictionary for words that
        contain the letters from the input. Takes a
        list as an argument. Calls two private functions
        to filter the results.
        """
        for word in self._words:
            if all(letter in letters for letter in word):
                self._results.append(word)
        self._filter_by_length()
        self._filter_by_primary(letters)

    def _filter_by_length(self):
        """
        Filters the results of the search to words that are
        at least 4 letters long and no longer than 10 letters.
        """
        new_results = []
        for word in self._results:
            if len(word) >= 4 and len(word) <= 10:
                new_results.append(word)
        self._results.clear()
        self._results = new_results

    def _filter_by_primary(self, letters):
        """
        Filters the results of the search to words that contain
        the primary letter. Takes a list as an argument.
        """
        new_results = []
        primary = letters[-1]
        for word in self._results:
            if primary in word:
                new_results.append(word)
        self._results.clear()
        self._results = new_results
    
    def get_results(self):
        """Getter function that returns the results variable."""
        return self._results