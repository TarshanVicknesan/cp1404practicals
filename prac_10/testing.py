import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeats string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """Checks if the word is as long or longer than the specified length."""
    return len(word) >= length


def run_tests():
    """Runs tests on the functions."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    test_car = Car()
    assert test_car._odometer == 0, "Odometer is not set correctly"

    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Fuel is not set correctly"

    test_car = Car()
    assert test_car.fuel == 0


def phrase_to_sentence(phrase):
    """Formats a phrase as a sentence, starting with a capital and ending with a period."""
    sentence = phrase.capitalize()
    if sentence[-1] != '.':
        sentence += '.'
    return sentence


run_tests()
doctest.testmod()
