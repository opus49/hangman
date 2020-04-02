"""Custom exceptions for hangman"""

class Error(Exception):
    """Base class for Hangman exceptions"""

class GuessError(Error):
    """Exception raised for an invalid guess"""
