import pytest 
from src.E_21 import *

@pytest.mark.parametrize(
    "input_x,expected",
    [
        ([120,80],200)
    ]
)

def test_calcularPago(input_x,expected):
    assert calcularPago(input_x) == expected


@pytest.mark.parametrize(
    "input_x,expected",
    [
        (200,"El total a pagar es: 200")
    ]
)

def test_mensajeSalida21(input_x,expected):
    assert mensajeSalida21(input_x) == expected