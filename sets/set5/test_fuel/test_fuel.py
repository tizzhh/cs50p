import pytest

from fuel import convert, gauge

def test_high():
    assert convert("3/4") == 75

def test_low():
    assert convert("1/4") == 25

def test_f():
    assert gauge(99) == "F"

def test_e():
    assert gauge(1) == "E"

def test_gauge():
    assert gauge(50) == "50%"

def test_str():
    with pytest.raises(ValueError):
        convert("three/four")

def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")