import pytest

from double_hanoi import solution, check_is_lower_in_left

test_data = [
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
def test_check_is_lower_in_left(aList, value, expected):
    result = check_is_lower_in_left(value, aList)
    assert result == expected
