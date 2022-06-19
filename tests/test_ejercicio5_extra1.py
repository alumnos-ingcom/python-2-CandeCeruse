################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio5_extra1 import *

"""
Estos test son una función que determine si una cadena con corchetes está balanceada.

Es decir, si cada corchete que abre, tiene su par que cierra. El resultado
debe ser un valor lógico indicando si esta o no balanceado.
"""

def test_balanceado():
    """
    Una breve descripción del caso de prueba aplicado a la función
    """
    caracter_apertura = "{"
    caracter_cierre = "}"
    cadena = '{}{{}}'
    resultado = determina_balance(cadena, caracter_apertura, caracter_cierre)
    assert isinstance(resultado, bool)
    assert resultado == True, "Debe ser True si está balanceado"

def test_desbalanceado():
    """
    Una breve descripción del caso de prueba aplicado a la función
    """
    caracter_apertura = "{"
    caracter_cierre = "}"
    cadena = '{{{{}}'
    resultado = determina_balance(cadena, caracter_apertura, caracter_cierre)
    assert isinstance(resultado, bool)
    assert resultado == False, "Debe ser False si está desbalanceado"