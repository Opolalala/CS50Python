from numb3rs import validate

def test_true():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.4") == True
    assert validate("1.200.32.41") == True
    assert validate("100.2.34.82") == True
    assert validate("126.255.30.48") == True
def test_false():
    assert validate("256.256.256.256") == False
    assert validate("1.2.3.400") == False
    assert validate("1.2.300.4") == False
    assert validate("1.260.3.4") == False
    assert validate("1000.2.3.4") == False
    assert validate("126.255.332.483") == False