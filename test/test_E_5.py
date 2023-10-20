import pytest 
from src.E_5 import *

@pytest.mark.parametrize(
    "input_x,expected",
    [
        (15.0,0.15)
    ]
)

def test_pasarPorcentaje(input_x,expected):
    assert pasarPorcentaje(input_x) == expected



@pytest.mark.parametrize(
    "input_x,input_y,input_z,expected",
    [
        (200.0,0.15,2,229.99999999999997)
    ]
)

def test_calculo(input_x,input_y,input_z,expected):
    assert calculo(input_x,input_y,input_z) == expected


@pytest.mark.parametrize(
    "input_x,expected",
    [
        (229.99999999999997,"El capital obtenido es: 229.99999999999997")
    ]
)

def test_mensajeSalida5(input_x,expected):
    assert mensajeSalida5(input_x) == expected