import pytest
from src.E_19 import *

@pytest.mark.parametrize(
    "expected",
    [
        ("Menú: \n1-Comenzar programa\n2-Imprimir listado\n3-Finalizar programa\n")
    ]
)

def test_menu(expected):
    assert menu() == expected

'''
@pytest.mark.parametrize(
    "expected",
    [
        ("Este es el listado.")
    ]
)

def test_imprimirListado(expected):
    assert imprimirListado() == expected


@pytest.mark.parametrize(
    "input_x,expected",
    [
        ("1","El programa ha comenzado"),
        ("2","Este es el listado."),
        ("3","El programa ha finalizado"),
        ("4","Opción incorrecta. Por favor, seleccione una opción válida.")
    ]
)

def test_accion(input_x,expected):
    assert accion(input_x) == expected 
'''