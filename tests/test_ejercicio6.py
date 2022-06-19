################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio6 import *

"""
Tests para un programa que toma un mensaje y lo encripta y
desencripta usando unicode y rotaciones.
"""

def test_unicode_a_texto():
    """
    Aqui pruebo convertir a texto el mensaje ya encriptado en unicode
    """
    texto = "CandeCapa3000"
    unicode = [79, 109, 122, 112, 113, 79, 109, 98, 109, 53, 50, 50, 50]
    salida = unicode_a_texto(texto, unicode)
    assert isinstance(salida, str), "La salida debe ser un string"
    assert salida == "OmzpqOmbm5222", "La salida debe estar codificada y ser un string"

def test_encriptado():
    """
    Aqui pruebo convertir el mensaje a unicode
    """
    texto = "CandeCapa3000"
    rotacion = 12
    unicode = encripta(texto, rotacion)
    assert isinstance(unicode, list), "La salida debe ser una lista"
    assert unicode == [79, 109, 122, 112, 113, 79, 109, 98, 109, 53, 50, 50, 50], "La salida debe ser el unicode encriptado"

def test_desencriptado():
    """
    Aqui pruebo convertir a texto el mensaje ya encriptado en unicode.
    Y devolver el mensaje con la rotacion.
    """
    encriptado = "OmzpqOmbm5222"
    rotacion = 12
    desencriptado = desencripta(encriptado, rotacion)
    assert isinstance(desencriptado, list), "La salida debe ser una lista"
    assert desencriptado == [67, 97, 110, 100, 101, 67, 97, 112, 97, 51, 48, 48, 48], "La salida debe ser el unicode desencriptado"