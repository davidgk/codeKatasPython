import pytest

from codewars.chords.example import chords

test_data =[
    (1, 1, 2),
    (3, 3, 6),
    (3, 4, 7),
]
params = "p1, p2, expected"


@pytest.mark.parametrize(params, test_data)
def test_chords(p1, p2, expected):
    result = chords(p1, p2)
    assert result == expected
