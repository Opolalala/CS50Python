from seasons import verify_date, get_min, min_to_words


def test_verify():
    assert verify_date("1990-02-02") == "1990-02-02"
    assert verify_date("2000-02-20") == "2000-02-20"


def test_get_min():
    assert get_min("1990-02-02") == 17994240
    assert get_min("2000-02-20") == 12709440


def test_min_to_words():
    assert min_to_words(17994240) == "seventeen million, nine hundred ninety-four thousand, two hundred forty"
    assert min_to_words(12709440) == "twelve million, seven hundred nine thousand, four hundred forty"