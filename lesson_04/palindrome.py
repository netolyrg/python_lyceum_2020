#


def is_palindrome(string):
    if not isinstance(string, str):
        return None

    if string == string[::-1]:
        return True
    else:
        return False
