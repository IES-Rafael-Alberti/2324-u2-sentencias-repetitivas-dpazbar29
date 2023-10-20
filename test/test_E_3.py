import pytest
from src.E_3 import *

@pytest.mark.parametrize(
    "input_x,expected",
    [
        (7,"1, 3, 5, 7")
    ]
)

def test_numerosImpares(input_x,expected):
    assert numerosImpares(input_x) == expected

@pytest.mark.parametrize(
    "input_x,expected",
    [
        ("1, 3, 5, 7","Numeros impares: 1, 3, 5, 7")
    ]
)

def test_mensajeSalida3(input_x,expected):
    assert mensajeSalida3(input_x) == expected