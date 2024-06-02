# Programmieren vertieft
# Aufgabe 4-a; 23.05.2024
# Name: Koji Okumura

from Aufgabe3_Koji import Author
import pytest

@pytest.fixture
def testauthor():
    "Return an Author object"
    return Author("Hammond", "Michael")

def test_init():
    "Test the __init__ method"
    testauthor = Author("Hammond", "Michael")
    assert testauthor.last_name == "Hammond"
    assert testauthor.first_name == "Michael"

def test_repr():
    "Test the __repr__ method"
    testauthor = Author("Hammond", "Michael")
    assert testauthor == "Hammond, Michael"
