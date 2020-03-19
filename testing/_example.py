from testing.example import is_year_leap


def test_leap():
    expected = True
    actual = is_year_leap(2020)

    assert expected == actual


def test_non_leap():
    expected = False
    actual = is_year_leap(2019)

    assert expected == actual

