"""Module for Game class"""

from hangman import Dictionary, Screen


class Game:
    """
    The primary object responsible for managing game details and flow.
    """
    def __init__(self):
        self._dictionary = Dictionary()

    def start(self):
        """Start the game"""
        self.game()
        self.quit()


    def game(self):
        """Play a single game of hangman"""

        # track the number of incorrect guesses
        guesses = 0

        # track the incorrect letters
        incorrect_letters = []

        # track the correct letters
        correct_letters = []

        # pick a word from the dictionary
        word = self._dictionary.get()

        # loop until the game is over
        result = None
        while result is not None:
            # show the gallows and incorrect guessses
            Screen.clear()
            Screen.gallows(len(incorrect_letters))

            # show the masked word

            # show incorrect guessses

            # ask the player for a guess
            guess = input("What is your guess? ")

            # handle that guess
            if guess in word:
                correct_letters.append(guess)
            else:
                incorrect_letters.append(guess)

            if len(incorrect_letters) > 5:
                result = False

        # display the results
