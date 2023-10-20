import pytest 
from src.E_8 import *

@pytest.mark.parametrize(
    "input_x,expected",
    [
        (3,"1 1 2 1 2 3")
    ]
)

def test_triangulo(input_x,expected):
    assert triangulo(input_x) == expected