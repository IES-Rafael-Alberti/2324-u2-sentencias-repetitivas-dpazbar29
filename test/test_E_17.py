import pytest 
from src.E_17 import * 

@pytest.mark.parametrize(
    "input_x,expected",
    [
        (12,3)
    ]
)

def test_sumaDigitos(input_x,expected):
    assert sumaDigitos(input_x) == expected


@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
        (12,3,"La suma de los dígitos de 12 es: 3")
    ]
)

def test_mensajeSalida17(input_x,input_y,expected):
    assert mensajeSalida17(input_x,input_y) == expected