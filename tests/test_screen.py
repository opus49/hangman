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

    def test_get(self):
        """Test the get method"""
        with mock.patch("builtins.input") as mock_input:
            mock_input.return_value = "foo"
            self.assertEqual(hangman.cli.screen.Screen.get("Foo?"), "foo")

    def test_put(self):
        """Test the put method"""
        with mock.patch("builtins.print") as mock_print:
            hangman.cli.screen.Screen.put("foo!")
            mock_print.assert_called_with("\nfoo!")

    def test_goodbye(self):
        """Test the goodbye method"""
        with mock.patch("builtins.print") as mock_print:
            hangman.cli.screen.Screen.goodbye()
            output = ",".join([str(x) for x in mock_print.call_args_list])
        self.assertTrue("Goodbye" in output)


if __name__ == "__main__":
    unittest.main()
