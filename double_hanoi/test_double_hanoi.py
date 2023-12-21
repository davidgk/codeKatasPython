import pytest

from double_hanoi import solution, check_is_lower, check_is_higher

test_data = [
    ([5, 2, 5, 2], 8, 1, 4),
    ([1, 4, 5, 5], 6, 4, 4),
    ([2, 3, 3, 4], 3, 1, 3),

]

params = "list_of_disks, leftIncreasing, rightDecreasing, expected"

@pytest.mark.parametrize(params, test_data)
def test_solution(list_of_disks, leftIncreasing, rightDecreasing, expected):
    assert solution(list_of_disks, leftIncreasing, rightDecreasing) == expected

test_data2 = [
    ([4, 2], 3, [4, 3, 2]),
    ([3, 2], 1, [3, 2, 1]),
    ([3, 2, 1], 1, [3, 2, 1]),
]

params2 = "aList, value, expected"

@pytest.mark.parametrize(params2, test_data2)
def test_check_is_lower(aList, value, expected):
    result = check_is_lower(value, aList)
    assert result == expected

test_data3 = [
    ([4, 7], 6, [4, 6, 7]),
    ([3, 4], 5, [3, 4, 5]),
    ([5, 6, 7], 7, [5, 6, 7]),
]

@pytest.mark.parametrize(params2, test_data3)
def test_check_is_higher(aList, value, expected):
    result = check_is_higher(value, aList)
    assert result == expected
