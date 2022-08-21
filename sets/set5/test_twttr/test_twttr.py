from twttr import shorten

def test_lower():
    assert shorten("twitter") == "twttr"

def test_upper():
    assert shorten("TWITTER") == "TWTTR"

def test_symbols():
    assert shorten("What's up twitter") == "Wht's p twttr"

def test_no_match():
    assert shorten("dddd") == "dddd"

def test_nubmers():
    assert shorten("123") == "123"

def test_first():
    assert shorten("itwitter") == "twttr"

def test_last():
    assert shorten("twitteri") == "twttr"

def test_punct():
    assert shorten(",") == ","