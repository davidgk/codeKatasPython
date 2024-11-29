import pytest

from codewars.find_uniq.example import find_uniq

test_data =[
    ([1, 2, 1, 1], 2),
    ([1, 1, 2, 1, 1], 2),
    ([1, 1, 2], 2),
    ([1, 1, 1, 2], 2),
    ([2, 1, 1], 2),
    ([2, 1, 1, 1], 2),

    ([1, 1, 2, 1], 2),

    ([1, 2, 1, 1, 1], 2),
]
params = "unique_value_, expected"


@pytest.mark.parametrize(params, test_data)
def test_find_uniq(unique_value_, expected):
    result = find_uniq(unique_value_)
    assert result == expected
