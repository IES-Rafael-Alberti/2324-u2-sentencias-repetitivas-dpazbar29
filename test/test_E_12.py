import pytest 
from src.E_12 import *

@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
        ("Buenas tardes","a",2)
    ]
)

def test_contarLetra(input_x,input_y,expected):
    assert contarLetra(input_x,input_y) == expected


@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
        ("a","2","La letra a aparece 2 veces")
    ]
)

def test_mensajeSalida12(input_x,input_y,expected):
    assert mensajeSalida12(input_x,input_y) == expected