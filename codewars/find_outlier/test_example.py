import pytest

from codewars.find_outlier.example import find_outlier, get_outlier_key

test_data = [
    ([1], -1),
    ([3, 2], -1),
    ([3, 2, 2], 3),
    ([2, 4, 0, 100, 4, 11, 2602, 36], 11),
    ([160, 3, 1719, 19, 11, 13, -21], 160),
]
params = "p1, expected"


@pytest.mark.parametrize(params, test_data)
def test_find_outlier(p1, expected):
    result = find_outlier(p1)
    assert result == expected


test_data_01 = [
    ([1, 1, 1], 0),
    ([1, 1, 2], 0),
    ([2, 2, 1], 1),
    ([2, 2, 2], 1),
]


@pytest.mark.parametrize(params, test_data_01)
def test_get_outlier_key(p1, expected):
    result = get_outlier_key(p1)
    assert result == expected
