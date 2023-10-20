import pytest 
from src.E_25 import *

@pytest.mark.parametrize(
    "input_x,expected",
    [
        ("Buenos días Jose","Buenos")
    ]
)

def test_encontarPalabra(input_x,expected):
    assert encontrarPalabra(input_x) == expected


@pytest.mark.parametrize(
    "input_x,expected",
    [
        ("Buenos días Jose",3)
    ]
)

def test_palabrasTotales(input_x,expected):
    assert palabrasTotales(input_x) == expected


@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
        ("Buenos",3,"La palabra mas larga es: Buenos\nEl número total de palabras es: 3")
    ]
)

def test_mensajeSalida25(input_x,input_y,expected):
    assert mensajeSalida25(input_x,input_y) == expected