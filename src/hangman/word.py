"""Module for interacting with a dictionary word"""

import re
from hangman.error import GuessError


class Word:
    """Interact with a raw dictionary word"""
    def __init__(self, raw_word):
        self._word = raw_word.upper()
        self._guesses = []
        self._valid_input_pattern = re.compile("^[A-Z]{1}$")

    @property
    def alive(self):
        """Is the hanging man still alive?"""
        return len(self.incorrects) < 6

    @property
    def incorrects(self):
        """Get a list of incorrect guesses"""
        return [x for x in self._guesses if x not in self._word]

    @property
    def masked(self):
        """The word with unguessed letters masked so the player cannot see them"""
        return " ".join([x if x in self._guesses else "_" for x in self._word])

    @property
    def solved(self):
        """Has the player solved the word?"""
        return "_" not in self.masked

    @property
    def unmasked(self):
        """The initial dictionary word without masking"""
        return self._word

    def guess(self, letter):
        """Apply a user's guess"""
        letter = letter.upper()
        if self._valid_input_pattern.match(letter):
            if letter not in self._guesses:
                self._guesses.append(letter)
            else:
                raise GuessError(f"ERROR: Already guessed letter {letter}")
        else:
            raise GuessError("ERROR: Please enter a single letter.")
