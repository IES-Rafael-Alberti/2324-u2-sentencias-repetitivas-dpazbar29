import pytest 
from src.E_9 import *

@pytest.mark.parametrize(
    "input_x,expected",
    [
        ("contraseña","¡La contraseña es correcta!"),
    ]
)

def test_comprobacion(input_x,expected):
    assert comprobacion(input_x) == expected
