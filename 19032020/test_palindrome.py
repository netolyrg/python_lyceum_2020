from palindrome import is_palindrome


def test_is_palindrome():
    word = '123321'
    expected = True
    actual = is_palindrome(word)

    assert expected == actual, 'Not expected output'


def test_not_palindrome():
    word = '123'
    expected = False
    actual = is_palindrome(word)

    assert expected == actual, 'Not expected output'


def test_incorrect_input():
    number = 1
    expected = None
    actual = is_palindrome(number)

    assert expected == actual
