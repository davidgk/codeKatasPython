import pytest

from codewars.story.example import story

test_data =[
    (1, 1, 2),
    (3, 3, 6),
    (3, 4, 7),
]
params = "p1, p2, expected"


@pytest.mark.parametrize(params, test_data)
def test_story(p1, p2, expected):
    result = story(p1, p2)
    assert result == expected
