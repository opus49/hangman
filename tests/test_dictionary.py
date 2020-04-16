#!/usr/bin/env python3

import unittest
import unittest.mock as mock

import context
import hangman.dictionary


class TestDictionary(unittest.TestCase):
    """Tests for Dictionary class"""

    def setUp(self):
        hangman.dictionary._WORDS = hangman.dictionary._WORDS[0:1000]
        self._dictionary = hangman.dictionary.Dictionary()

    def test_init_handles_excluded_words(self):
        """test that the constructor handles excluded words"""
        my_dictionary = hangman.dictionary.Dictionary(["aardvark"])
        with mock.patch("hangman.dictionary.randint", return_value=0):
            self.assertNotEqual(
                my_dictionary.get(),
                "aardvark"
            )

    def test_get(self):
        """test the get method"""
        with mock.patch("hangman.dictionary.randint", return_value=0):
            for index in range(len(hangman.dictionary._WORDS)):
                self.assertEqual(
                    self._dictionary.get(),
                    hangman.dictionary._WORDS[index]
                )

    def test_get_throws_error(self):
        """test that get throws an error when it runs out of words"""
        my_dictionary = hangman.dictionary.Dictionary(hangman.dictionary._WORDS)
        with self.assertRaises(ValueError):
            my_dictionary.get()


if __name__ == "__main__":
    unittest.main()
