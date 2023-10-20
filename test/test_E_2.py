import pytest 
from src.E_2 import *

@pytest.mark.parametrize(
    "input_x,expected",
    [
        (18,'[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]')
    ]
)

def test_secuencia(input_x,expected):
    assert secuencia(input_x) == expected

@pytest.mark.parametrize(
    "input_x,expected",
    [
        ('[1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14 ,15 ,16 ,17 ,18]','Resultado: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14 ,15 ,16 ,17 ,18]')
    ]
)

def test_mensajeSalida2(input_x,expected):
    assert mensajeSalida2(input_x) == expected