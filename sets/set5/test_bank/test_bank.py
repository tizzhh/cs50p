from bank import value

def test_0():
    assert value("hello") == 0

def test_20():
    assert value("hi") == 20

def test_100():
    assert value("what") == 100

def test_upper():
    assert value("WHAT") == 100

def test_lower():
    assert value("HELLO") == 0
