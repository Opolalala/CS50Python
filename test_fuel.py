from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("2/3") == 67


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(75) == "75%"
    assert gauge(50) == "50%"
    assert gauge(67) == "67%"


def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_value():
    with pytest.raises(ValueError):
        convert("4/3")