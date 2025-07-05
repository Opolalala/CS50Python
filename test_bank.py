from bank import value


def test_cap():
    assert value("HEY BOO") == 20
    assert value("HOLA HABIBI") == 20


def test_hello():
    assert value("hello") == 0
    assert value("hello, world") == 0


def test_hey():
    assert value("hey") == 20
    assert value("how") == 20


def test_not_h():
    assert value("random") == 100
    assert value("vampire") == 100