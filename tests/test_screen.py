#!/usr/bin/env python3

"""Unit tests for screen module"""

import unittest
import unittest.mock as mock

import context
import hangman.cli.screen


class TestScreen(unittest.TestCase):
    """Tests for Screen class"""

    @mock.patch("hangman.cli.screen.os.name", "nt")
    def test_clear_windows(self):
        """Test the clear method works for NT-based systems"""
        with mock.patch("hangman.cli.screen.os.system") as mock_system:
            hangman.cli.screen.Screen.clear()
            mock_system.assert_called_with("cls")

    @mock.patch("hangman.cli.screen.os.name", "posix")
    def test_clear_posix(self):
        """Test the clear method works for posix-based systems"""
        with mock.patch("hangman.cli.screen.os.system") as mock_system:
            hangman.cli.screen.Screen.clear()
            mock_system.assert_called_with("clear")

    def test_gallows_within_bounds(self):
        """Test to see if the gallows method returns the correct image"""
        with mock.patch("hangman.cli.screen.print") as mock_print:
            for index in range(len(hangman.cli.screen._GALLOWS)):
                hangman.cli.screen.Screen.gallows(index)
                mock_print.assert_called_with(hangman.cli.screen._GALLOWS[index])

    def test_gallows_outside_bounds(self):
        """Test the gallows method handles out of bounds indices"""
        with mock.patch("hangman.cli.screen.print") as mock_print:
            for index in [-1, len(hangman.cli.screen._GALLOWS)]:
                hangman.cli.screen.Screen.gallows(index)
                mock_print.assert_called_with(hangman.cli.screen._GALLOWS[-1])


if __name__ == "__main__":
    unittest.main()
