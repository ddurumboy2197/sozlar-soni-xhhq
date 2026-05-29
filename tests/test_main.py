# test_gap.py
import pytest
from gap import Gap

def test_gap():
    gap = Gap("Hello, world!")
    assert gap.count_words() == 5

def test_gap_empty_string():
    gap = Gap("")
    assert gap.count_words() == 0

def test_gap_single_word():
    gap = Gap("Hello")
    assert gap.count_words() == 1

def test_gap_multiple_gaps():
    gap = Gap("Hello, world!  This is a test.")
    assert gap.count_words() == 7
