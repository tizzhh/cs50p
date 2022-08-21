from seasons import convert

def test_1():
    assert convert("2021-08-13") == 525600

def test_2():
    assert convert("2020-08-13") == 1051200