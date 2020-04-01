# test find_quadratic_equation_roots

from tasks_04.quadratic_equation_roots import find_quadratic_equation_roots


def test_two_roots():
    a, b, c = 1, 2, -3
    expected = (1, -3)
    actual = find_quadratic_equation_roots(a, b, c)

    assert len(actual) == 2
    assert sorted(expected) == sorted(actual)
