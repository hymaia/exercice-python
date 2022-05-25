# TODO : importer le framework de test et compléter la class
from src.wordcount import *


def test_wordcount():
    # GIVEN
    input = "Bonjour bonjour, je m'appelle Franck"
    expected = [('Bonjour', 1), ('bonjour,', 1), ('je', 1), ("m'appelle", 1), ('Franck', 1)]

    # WHEN
    actual = wordcount(input)

    # THEN
    assert expected == actual

def test_clean_wordcount():
    # GIVEN
    input = clean_text("Bonjour bonjour, je m'appelle Franck")
    expected = [('bonjour', 2), ('je', 1), ('m', 1), ('appelle', 1), ('franck', 1)]

    # WHEN
    actual = wordcount(input)

    # THEN
    assert expected == actual

def test_clean_text():
    # GIVEN
    input = "Bonjour bonjour, je m'appelle Franck"
    expected = "bonjour bonjour  je m appelle franck"

    # WHEN
    actual = clean_text(input)

    # THEN
    assert actual == expected
