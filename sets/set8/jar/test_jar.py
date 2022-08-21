from jar import Jar

import pytest


def test_init():
    jar = Jar(10)
    assert jar.capacity == 10


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2

def test_deposit_ValueError():
    jar = Jar(1)
    with pytest.raises(ValueError):
        jar.deposit(2)

def test_withdraw():
    jar = Jar()
    jar.deposit(3)
    jar.withdraw(1)
    assert jar.size == 2

def test_withdraw_ValueError():
    jar = Jar()
    jar.deposit(3)
    with pytest.raises(ValueError):
        jar.withdraw(4)