import pytest

from codewars.credit_card_mask.example import maskify

test_data =[
    ("Skippy", "##ippy"),
    ("64607935616", "#######5616"),
    ("4556364607935616", "############5616"),
    ("1", "1"),
    ("", ""),
    ("Nananananananananananananananana Batman!", "####################################man!")
]
params = "p1, expected"


@pytest.mark.parametrize(params, test_data)
def test_maskify(p1, expected):
    result = maskify(p1)
    assert result == expected
