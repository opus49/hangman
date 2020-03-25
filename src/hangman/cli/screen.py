import os


_GALLOWS = [
    """
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
    """
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
    """
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
    """
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
    """
    =============
    ||/     |
    ||     ( )
    ||     _|_
    ||    / | \\
    ||      |
    ||
    ||
    ||
    """,
    """
    =============
    ||/     |
    ||     ( )
    ||     _|_
    ||    / | \\
    ||      |
    ||    _/
    ||
    ||
    """,
    """
    =============
    ||/     |
    ||     ( )
    ||     _|_
    ||    / | \\
    ||      |
    ||    _/ \_
    ||
    ||
    """
]


class Screen:
    @staticmethod
    def clear():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    @staticmethod
    def gallows(guesses):
        try:
            print(_GALLOWS[guesses])
        except IndexError:
            print(_GALLOWS[-1])
