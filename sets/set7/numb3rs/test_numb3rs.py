from numb3rs import validate

def test_single_dig():
    assert validate("1.2.3.4") == True

def test_two_dig():
    assert validate("10.20.30.40") == True


def test_three_dig():
    assert validate("100.200.255.255") == True
    assert validate("100.200.300.400") == False

def test_string():
    assert validate("cat") == False