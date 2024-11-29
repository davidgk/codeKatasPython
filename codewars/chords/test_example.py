import pytest

from codewars.blank.example import solution

test_data =[
    (1, 1, 2),
    (3, 3, 6),
    (3, 4, 7),
]
params = "p1, p2, expected"


@pytest.mark.parametrize(params, test_data)
def test_solution(p1, p2, expected):
    result = solution(p1, p2)
    assert result == expected
