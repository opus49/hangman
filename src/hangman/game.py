"""Module for Game class"""

import time

from hangman import Dictionary
from hangman.cli.screen import Screen
from hangman.word import Word
from hangman.error import GuessError


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
        word = Word(self._dictionary.get())
        while True:
            Screen.clear()
            Screen.gallows(len(word.incorrects))
            word.show()
            if not word.alive or word.solved:
                break
            guess = input("\nWhat is your guess? ")
            try:
                word.guess(guess)
            except GuessError as err:
                print(err)
                time.sleep(2)
        if word.alive:
            print("\nCongrats, you won!!")
        else:
            print(f"\nI'm sorry.  The word was {word.unmasked}.")

    @staticmethod
    def quit():
        """Quit the game"""
        print("\n")
        print("=" * 50)
        print(" " * 20, "Goodbye!")
        print("=" * 50)
        print("\n\n")
