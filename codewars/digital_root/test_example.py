import pytest

from codewars.digital_root.example import digital_root
test_data =[
    (10, 1),
    (16, 7),
    (942, 6),
    (132189, 6),
    (493193, 2),
    (1, 1),
    (9, 9),
    (0, 0),
    (None, 0),
]

params = "p1, expected"


@pytest.mark.parametrize(params, test_data)
def test_solution(p1, expected):
    result = digital_root(p1)
    assert result == expected
