################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio3 import *

"""
Caso de prueba para un programa que compara cadenas
y devuelve la superposicion de las mismas.
"""

def test_cadenas_superponen():
    """
    Si las cadenas son completamente distintas
    """
    cadena_1 = "Hola Mundo"
    cadena_2 = "Quee Mundo?"
    superposicion = compara_cadenas(cadena_1, cadena_2)
    assert isinstance(superposicion, int), "El resultado debe ser un int"
    assert superposicion == 6, "EL resultado debe ser la cantidad de superposicion"

def test_cadenas_no_superponen():
    """
    Si las cadenas son completamente distintas
    """
    cadena_1 = "Hola Mundo"
    cadena_2 = "Que Pex?"
    superposicion = compara_cadenas(cadena_1, cadena_2)
    assert isinstance(superposicion, int), "El resultado debe ser un int"
    assert superposicion == 0, "EL resultado debe ser cero porque no hay superposicion"