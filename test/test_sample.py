"""Pytest sample"""
import pytest

def isOdd(n):
    return n % 2 != 0

def isEven(n):
    return n % 2 == 0

def test_is_odd():
    assert isOdd(3) == True
    assert isOdd(4) == False

def test_is_even():
    assert isEven(3) == False
    assert isEven(4) == True