import pytest 
from src.E_7 import *

@pytest.mark.parametrize(
    "input_x,expected",
    [
        (3,"3 * 1 = 3\n3 * 2 = 6\n3 * 3 = 9\n3 * 4 = 12\n3 * 5 = 15\n3 * 6 = 18\n3 * 7 = 21\n3 * 8 = 24\n3 * 9 = 27\n3 * 10 = 30")
    ]
)

def test_tabla(input_x,expected):
    assert tabla(input_x) == expected