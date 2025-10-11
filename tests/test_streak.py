import pytest
from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    assert longest_positive_streak([-1, -2, -3, 0]) == 0

def test_all_positive_numbers():
    assert longest_positive_streak([1, 2, 3, 4]) == 4

def test_multiple_streaks():
    assert longest_positive_streak([1, 2, 0, 4, 5, 6, -1, 8]) == 3

def test_streaks_with_negatives_and_zeros():
    assert longest_positive_streak([1, 2, -3, 4, 0, 5, 6, 7]) == 3

def test_single_element_list():
    assert longest_positive_streak([1]) == 1
    assert longest_positive_streak([-1]) == 0
    assert longest_positive_streak([0]) == 0

def test_streak_at_beginning():
    assert longest_positive_streak([1, 2, 3, 0, -1, -2]) == 3

def test_streak_at_end():
    assert longest_positive_streak([-1, 0, 1, 2, 3, 4]) == 4