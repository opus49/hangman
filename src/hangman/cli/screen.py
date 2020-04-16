"""Module for dealing with the screen for Hangman game"""

import os


_GALLOWS = [
    r"""
    =============
    ||/     |
    ||
    ||
    ||
    ||
    ||
    ||
    ||
    """,
    r"""
    =============
    ||/     |
    ||     ( )
    ||
    ||
    ||
    ||
    ||
    ||
    """,
    r"""
    =============
    ||/     |
    ||     ( )
    ||      |
    ||      |
    ||      |
    ||
    ||
    ||
    """,
    r"""
    =============
    ||/     |
    ||     ( )
    ||     _|
    ||    / |
    ||      |
    ||
    ||
    ||
    """,
    r"""
    =============
    ||/     |
    ||     ( )
    ||     _|_
    ||    / | \
    ||      |
    ||
    ||
    ||
    """,
    r"""
    =============
    ||/     |
    ||     ( )
    ||     _|_
    ||    / | \
    ||      |
    ||    _/
    ||
    ||
    """,
    r"""
    =============
    ||/     |
    ||     ( )
    ||     _|_
    ||    / | \
    ||      |
    ||    _/ \_
    ||
    ||
    """
]


class Screen:
    """Interface to screen"""
    @staticmethod
    def clear():
        """Clear the screen"""
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    @staticmethod
    def gallows(guesses):
        """Show the gallows based on the number of incorrect guesses"""
        try:
            print(_GALLOWS[guesses])
        except IndexError:
            print(_GALLOWS[-1])

    @staticmethod
    def get(question):
        """Ask the user a question and return the answer"""
        return input(f"\n{question} ")

    @staticmethod
    def goodbye():
        """Say goodbye to the user"""
        print("\n")
        print("=" * 50)
        print(" " * 20, "Goodbye!")
        print("=" * 50)
        print("\n\n")

    @staticmethod
    def put(message):
        """Print a message to the user"""
        print(f"\n{message}")
