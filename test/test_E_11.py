import pytest 
from src.E_11 import *

@pytest.mark.parametrize(
    "input_x,expected",
    [
        ("dani","i n a d")
    ]
)

def test_mostrarLetras(input_x,expected):
    assert mostrarLetras(input_x) == expected


@pytest.mark.parametrize(
    "input_x,expected",
    [
        ("i n a d","Resultado: i n a d")
    ]
)

def test_mensajeSalida11(input_x,expected):
    assert mensajeSalida11(input_x) == expected