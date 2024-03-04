import pytest

from codewars.pangrams.example import solution

test_data =[
    ("; 5 abc d", False),
    (1, False),
    ("; 5 aBC d", False),
    ("ab cd ef;  gh ij k", False),
    ("ab cde fgh ij klmnopq rstuv. wxyz", True),
    ("ab cde fgh ij klMnopq 12345 rstuv. Wxyz", True),
    ("ab cde fgh ij klMnopq 12345 rstuv. Wxyz ABCD E", True),
]
params = "p1, expected"


@pytest.mark.parametrize(params, test_data)
def test_solution(p1, expected):
     assert solution(p1) == expected
