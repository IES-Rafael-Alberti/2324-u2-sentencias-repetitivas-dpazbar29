'''
import pytest 
from src.E_24 import *

@pytest.mark.parametrize(
    "input_x,expected",
    [
        (1,True)
    ]
)

def test_esPrimo(input_x,expected):
    assert esPrimo(input_x) == expected
'''

#NO REALIZADO