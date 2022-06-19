################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio3_extra import *

"""
Caso de prueba para un programa que compara cadenas
y devuelve la superposicion de las mismas.
"""

def test_cadenas_superponen():
    """
    Si las cadenas son completamente distintas
    """
    cadena_1 = "HolaMundo"
    cadena_2 = "QueeMundo?"
    superposicion = compara_cadenas(cadena_1, cadena_2)
    assert isinstance(superposicion, int), "El resultado debe ser un int"
    assert superposicion == 4, "EL resultado debe ser la posicion de la superposicion"

def test_cadenas_no_superponen():
    """
    Si las cadenas son completamente distintas
    """
    cadena_1 = "HolaMundo"
    cadena_2 = "Que Pex?"
    superposicion = compara_cadenas(cadena_1, cadena_2)
    assert superposicion == None, "EL resultado debe ser None porque no hay superposicion"