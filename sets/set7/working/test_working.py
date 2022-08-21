from working import convert

import pytest

def test_first():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_second():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_third():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

def test_fourth():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_valerr():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_valerr1():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_valerr2():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")

def test_valer3():
    with pytest.raises(ValueError):
        convert("09:00 XM - 17:00 YM")

def test_valer4():
    with pytest.raises(ValueError):
        convert("9AM to 5PM")

def test_valer5():
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")

def test_valer6():
    with pytest.raises(ValueError):
        convert("10:7 AM - 5:1 PM")