# Programmieren vertieft
# Aufgabe 4-c; 23.05.2024
# Name: Koji Okumura

from Aufgabe3_Koji import Book
import pytest

@pytest.fixture
def testbook():
    "Return an Book object"
    return Book("Python for Linguists", 2018, "Hammond, Michael", "Cambridge: Cambridge University Press")

def test_init_year_as_int():
    "Test the __init__ method using an int as yaer"
    testbook = Book("Python for Linguists", 2018, "Hammond, Michael", "Cambridge: Cambridge University Press")
    assert testbook.title == "Python for Linguists"
    assert testbook.year == 2018
    assert testbook.author == "Hammond, Michael"
    assert testbook.publisher == "Cambridge: Cambridge University Press"

def test_init_year_as_str():
    "Test the __init__ method using a str as yaer"
    testbook = Book("Python for Linguists", "2018", "Hammond, Michael", "Cambridge: Cambridge University Press")
    assert testbook.title == "Python for Linguists"
    assert testbook.year == 2018
    assert testbook.author == "Hammond, Michael"
    assert testbook.publisher == "Cambridge: Cambridge University Press"

def test_repr():
    "Test the __repr__ method"
    assert testbook == "Title: Python for Linguists; Year: 2018; Author: Hammond, Michael; Publisher: Cambridge: Cambridge University Press"

def test_get_citation():
    "Test the get_citation method"
    assert testbook.get_citation() == "Hammond, Michael (2018). Python for Linguists. Cambridge: Cambridge University Press"
