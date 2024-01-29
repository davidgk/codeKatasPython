import pytest
from max_square_matrix import max_squares

test_data =[
    ([2, 2, 3, 3, 3], 3),
    ([2, 2, 1], 2),
    ([4, 2, 1], -1),
]
params = "board, expected"


@pytest.mark.parametrize(params, test_data)
def test_solution(board, expected):
    assert max_squares(board) == expected
