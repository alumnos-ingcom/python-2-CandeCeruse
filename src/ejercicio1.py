################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
1. Pares e impares

Escribir una función que retorne True cuando un número entero es par
y False cuando no lo sea, sin utilizar módulo. (%)
"""
def es_par(numero):
    """
    Esta funcion comprueba si el numero es entero.
    Devuleve true si lo es y False si no lo es.
    """
    cociente = numero / 2
    cociente_entero = numero // 2
    resultado = cociente - cociente_entero
    if resultado == 0:
        respuesta = True
    else:
        respuesta = False

    return respuesta


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input("Ingrese numero entero: "))
    respuesta = es_par(numero)
    if respuesta:
        print("Es par")
    else:
        print("No es par")


if __name__ == "__main__":
    principal()
