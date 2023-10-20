import pytest
from src.E_1 import *

@pytest.mark.parametrize(
    "input_x,expected",
    [
        ("hola","hola hola hola hola hola hola hola hola hola hola")
    ]
)

def test_repeticion(input_x,expected):
    assert repeticion(input_x) == expected

@pytest.mark.parametrize(
    "input_x,expected",
    [
        ("hola hola hola hola hola hola hola hola hola hola","Resultado: hola hola hola hola hola hola hola hola hola hola")
    ]
)

def test_mensajeSalida1(input_x,expected):
    assert mensajeSalida1(input_x) == expected