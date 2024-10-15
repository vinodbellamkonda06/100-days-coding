import pytest

from implementation.second_largest_number import  second_large_number


@pytest.mark.parametrize("input, expected", [([10, 20, 3, 45, 6,34, 9], 34),
                                             ([3, 4], 3),
                                             ([5, 5, 5], 5),
                                             ([], "empty")])
def test_second_largest_number(input, expected):
    assert second_large_number(input) == expected

