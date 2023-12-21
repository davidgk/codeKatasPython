import pytest

from double_hanoi import solution, add_values

test_data =[
    ([2, 3, 3, 4], 3, 1, 1),
]

params = "list_of_disks, leftIncreasing, rightDecreasing, expected"

@pytest.mark.parametrize(params, test_data)
def test_solution(list_of_disks, leftIncreasing, rightDecreasing, expected):
    assert solution(list_of_disks, leftIncreasing, rightDecreasing) == 1




