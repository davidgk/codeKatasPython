import pytest

from double_hanoi import solution, evaluate_info

test_data = [
    ([1, 5, 5], 2, 4, 2),
    ([5, 2, 5, 2], 8, 1, 4),
    ([1, 4, 5, 5], 6, 4, 4),
    ([2, 3, 3, 4], 3, 1, 3),
]

params = "list_of_disks, leftIncreasing, rightDecreasing, expected"

@pytest.mark.parametrize(params, test_data)
def test_solution(list_of_disks, leftIncreasing, rightDecreasing, expected):
    assert solution(list_of_disks, leftIncreasing, rightDecreasing) == expected

params2 = "aList, value, isLower,  expected"

test_data3 = [
    ([4, 2], 3, True, [4, 3, 2]),
    ([3, 2], 1, True, [3, 2, 1]),
    ([3, 2, 1], 1, True, [3, 2, 1]),
    ([4, 7], 6, False, [4, 6, 7]),
    ([3, 4], 5, False, [3, 4, 5]),
    ([5, 6, 7], 7, False, [5, 6, 7]),
]

@pytest.mark.parametrize(params2, test_data3)
def test_evaluate_info(aList, value, isLower, expected):
    result = evaluate_info(value, aList, isLower)
    assert result == expected

