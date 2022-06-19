################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio1 import es_par

"""
Casos de prueba para comprobar si un numero es par.
"""


def test_es_par():
    """
    Una breve descripción del caso de prueba aplicado a la función
    """
    numero = 24
    resultado = es_par(numero)
    assert isinstance(numero, int), "El numero ingresado debe ser un entero"
    assert isinstance(resultado, bool), "El resultado debe ser booleano"
    assert resultado == True, "El resultado debe ser true"

def test_no_es_par():
    """
    Una breve descripción del caso de prueba aplicado a la función
    """
    numero = 21
    resultado = es_par(numero)
    assert isinstance(numero, int), "El numero ingresado debe ser un entero"
    assert isinstance(resultado, bool), "El resultado debe ser booleano"
    assert resultado == False, "El resultado debe ser false"