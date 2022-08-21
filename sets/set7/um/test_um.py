from um import count

def test_single():
    assert count("um") == 1

def test_single_symbol():
    assert count("um?") == 1

def test_single_sentence():
    assert count("Um, thanks for the album.") == 1

def test_multiple():
    assert count("Um, thanks, um...") == 2