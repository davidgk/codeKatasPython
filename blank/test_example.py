import pytest
from example import add_values

test_data =[
    (1, 1, 2),
    (3, 3, 6),
    (3, 4, 7),
]
params = "p1, p2, expected"


@pytest.mark.parametrize(params, test_data)
def test_solution(p1, p2, expected):
    assert add_values(p1, p2) == expected
