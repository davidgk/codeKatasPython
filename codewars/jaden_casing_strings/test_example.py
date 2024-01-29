import pytest

from codewars.jaden_casing_strings.example import solution

test_data =[
    ("how", "How"),
    ("how are you", "How Are You"),
    ("don't you know what I mean?", "Don't You Know What I Mean?"),

]
params = "p1, expected"


@pytest.mark.parametrize(params, test_data)
def test_solution(p1, expected):
    assert solution(p1) == expected
