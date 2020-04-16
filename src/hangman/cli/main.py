#!/usr/bin/env python3

"""Main entry point for Hangman game"""

from hangman import Game


def main():
    """main function"""
    game = Game()
    game.start()


if __name__ == "__main__":
    main()
