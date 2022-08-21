from plates import is_valid

def test_short():
    assert is_valid("AA") == True
    assert is_valid("A1") == False

def test_not_alpha_start():
    assert is_valid("1A") == False
    assert is_valid("1") == False
    assert is_valid("11") == False

def test_right_len():
    assert is_valid("H") == False
    assert is_valid("TOOMANYLETTERS") == False

def test_2l2n():
    assert is_valid("CS50") == True

def test_case_case_insensitivity():
    assert is_valid("cs50") == True

def test_2l2n_first0():
    assert is_valid("CS05") == False

def test_no_letters_after_numbers():
    assert is_valid("CS50P") == False

def test_no_junk():
    assert is_valid("PI3.14") == False