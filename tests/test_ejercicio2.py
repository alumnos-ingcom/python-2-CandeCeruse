################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio2 import *

"""
Casos de prueba para analisis de una tupla de 10 numeros
ingresados por el usuario
"""

def test_maximos():
    """
    si el resultado es un int
    """
    cadena = (1, 0, 2, 3, -45, 123, 0, 65, 12, 65)
    maximo = busca_maximo(cadena)
    assert isinstance(maximo, int), "El resultado debe ser un entero"
    assert maximo == 123, "Debe mostrar el valor maximo"
    
def test_minimos():
    """
    si el resultado es un int
    """
    cadena = (1, 0, 2, 3, -45, 123, 0, 65, 12, 65)
    minimo = busca_minimo(cadena)
    assert isinstance(minimo, int), "El resultado debe ser un entero"
    assert minimo == -45, "Debe mostrar el valor minimo"

def test_promedio():
    cadena = (1, 0, 2, 3, -45, 123, 0, 65, 12, 65)
    promedio = promedia(cadena)
    assert isinstance(promedio, float), "El resultado debe ser un float"
    assert promedio == 22.6, "Debe mostrar el promedio"
    