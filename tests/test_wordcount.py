import unittest

from src.wordcount import *


class TestTransform(unittest.TestCase):
    def test_wordcount(self):
        # GIVEN
        input_str = "Bonjour bonjour, je m'appelle Franck"
        expected = [('Bonjour', 1), ('bonjour,', 1), ('je', 1), ("m'appelle", 1), ('Franck', 1)]

        # WHEN
        actual = wordcount(input_str)

        # THEN
        self.assertEqual(expected, actual)

    def test_clean_wordcount(self):
        # GIVEN
        input_str = clean_text("Bonjour bonjour, je m'appelle Franck")
        expected = [('bonjour', 2), ('je', 1), ('m', 1), ('appelle', 1), ('franck', 1)]

        # WHEN
        actual = wordcount(input_str)

        # THEN
        self.assertEqual(expected, actual)

    def test_clean_text(self):
        # GIVEN
        input_str = "Bonjour bonjour, je m'appelle Franck"
        expected = "bonjour bonjour  je m appelle franck"

        # WHEN
        actual = clean_text(input_str)

        # THEN
        self.assertEqual(expected, actual)
