import pytest 
from src.E_4 import *

@pytest.mark.parametrize(
    "input_x,expected",
    [
        (5,"5, 4, 3, 2, 1, 0")
    ]
)

def test_cuentaAtras(input_x,expected):
    assert cuentaAtras(input_x) == expected

@pytest.mark.parametrize(
    "input_x,expected",
    [
        ("5, 4, 3, 2, 1, 0","Cuenta atrás: 5, 4, 3, 2, 1, 0")
    ]
)

def test_mensajeSalida4(input_x,expected):
    assert mensajeSalida4(input_x) == expected