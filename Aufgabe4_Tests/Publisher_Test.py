# Programmieren vertieft
# Aufgabe 4-b; 23.05.2024
# Name: Koji Okumura

from Aufgabe3_Koji import Publisher
import pytest

@pytest.fixture
def testpublisher():
    "Return an Publisher object"
    return Publisher("Cambridge University Press", "Cambridge")

def test_init():
    "Test the __init__ method"
    testpublsiher = Publisher("Cambridge University Press", "Cambridge")
    assert testpublsiher.publisher == "Cambridge University Press"
    assert testpublsiher.place == "Cambridge"

def test_repr():
    "Test the __repr__ method"
    testpublsiher = Publisher("Cambridge University Press", "Cambridge")
    assert testpublsiher == "Cambridge: Cambridge University Press"
