import pytest 
from src.E_10 import *

@pytest.mark.parametrize(
    "input_x,expected",
    [
        (1,True),
        (2,False),
        (67,True)
    ]
)

def test_primo(input_x,expected):
    assert primo(input_x) == expected