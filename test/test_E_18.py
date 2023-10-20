'''
import pytest
from src.E_18 import *

@pytest.mark.parametrize(
    "input_x,expected",
    [
        (14,5)
    ]
)

def test_sumaDigitos18(input_x,expected):
    assert sumaDigitos18(input_x) == expected


@pytest.mark.parametrize(
    "input_x,expected",
    [
        (14,1)
    ]
)

def test_contarPares(input_x,expected):
    assert contarPares(input_x) == expected


@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
        (14,5,"La suma de los dígitos de 14 es: 5")
    ]
)

def test_mensajeSalida18Suma(input_x,input_y,expected):
    assert mensajeSalida18Suma(input_x,input_y) == expected


@pytest.mark.parametrize(
    "input_x,expected",
    [
        (2,"La cantidad de numeros pares ingresados fue 2")
    ]
)

def test_mensajeSalida18Pares(input_x,expected):
    assert mensajeSalida18Pares(input_x) == expected
'''
