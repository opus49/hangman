"""Module for Game class"""

import time

from hangman.dictionary import Dictionary
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
            Screen.put(f"Word      : {word.masked}")
            Screen.put(f"Incorrects: {' '.join(word.incorrects)}")
            if not word.alive or word.solved:
                break
            guess = Screen.get("What is your guess?")
            try:
                word.guess(guess)
            except GuessError as err:
                Screen.put(str(err))
                time.sleep(2)
        if word.alive:
            Screen.put("Congrats, you won!!")
        else:
            Screen.put(f"I'm sorry.  The word was {word.unmasked}.")

    @staticmethod
    def quit():
        """Quit the game"""
        Screen.goodbye()
