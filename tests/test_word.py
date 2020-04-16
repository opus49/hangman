#!/usr/bin/env python3

import unittest
import unittest.mock as mock

import context
import hangman.error
import hangman.word


class TestWord(unittest.TestCase):
    """Tests for Word class"""

    def setUp(self):
        self._word = hangman.word.Word("piZZa")

    def test_alive_return_true(self):
        """Test alive property correctly returns True"""
        self.assertTrue(self._word.alive)

    def test_alive_return_false(self):
        """Test alive property correctly returns False"""
        self._word._guesses = ["A", "B", "C", "D", "E", "F", "G"]
        self.assertFalse(self._word.alive)

    def test_incorrects(self):
        """Test the incorrects property returns correct letters"""
        self._word.guess("P")
        self._word.guess("B")
        self._word.guess("C")
        self.assertEqual(self._word.incorrects, ["B", "C"])

    def test_masked(self):
        """Test the masked property works correctly"""
        self.assertEqual(self._word.masked, "_ _ _ _ _")
        self._word.guess("Z")
        self._word.guess("B")
        self._word.guess("P")
        self.assertEqual(self._word.masked, "P _ Z Z _")

    def test_solved(self):
        """Test the solved property returns True properly"""
        self.assertFalse(self._word.solved)
        self._word.guess("P")
        self._word.guess("I")
        self._word.guess("Z")
        self._word.guess("A")
        self.assertTrue(self._word.solved)

    def test_unmasked(self):
        """Test the unmasked property"""
        self.assertEqual(self._word.unmasked, "PIZZA")
        self.assertNotEqual(self._word.unmasked, "pizza")

    def test_guess_correct_letter(self):
        """Test the guess method handles a correct letter"""
        self._word.guess("z")
        self._word.guess("P")
        self.assertEqual(self._word.masked, "P _ Z Z _")
        self.assertEqual(self._word.incorrects, [])

    def test_guess_incorrect_letter(self):
        """Test the guess method handles an incorrect letter"""
        self.assertEqual(self._word.incorrects, [])
        self._word.guess("b")
        self._word.guess("C")
        self._word.guess("a")
        self.assertEqual(self._word.incorrects, ["B", "C"])

    def test_guess_invalid_input(self):
        """Test the guess method handles invalid input correctly"""
        for guess in ["aaa", "1", "!"]:
            with self.assertRaises(hangman.error.GuessError):
                self._word.guess(guess)

    def test_guess_duplicate_letter(self):
        """Test the guess method handles a duplicate letter"""
        self._word.guess("a")
        with self.assertRaises(hangman.error.GuessError):
            self._word.guess("a")
        self._word.guess("B")
        with self.assertRaises(hangman.error.GuessError):
            self._word.guess("B")


if __name__ == "__main__":
    unittest.main()
