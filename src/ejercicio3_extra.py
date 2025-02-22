################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
3. Súper-puestos EXTRA

Desarrollar una función que indique el grado de superposición
entre dos listas. Indicar en lugar de la cantidad de caracteres superpuestos,
la posicion de inicio de la superposición.
"""
# Reemplazar por las funciones del ejercicio

def compara_cadenas(cadena_1, cadena_2):
    """
    Esta funcion compara las cadenas hasta el largo de
    la cadena mas corta.
    Devuelve un int con la cantidad de coincidencias.
    """
    superposicion = 0
    posicion = 0
    if len(cadena_1) >= len(cadena_2):
        limite = len(cadena_2)
    elif len(cadena_2) > len(cadena_1):
        limite = len(cadena_1)
    while limite > 0:
        if cadena_1[posicion] == cadena_2[posicion]:
            superposicion = posicion
            break
        else:
            superposicion = None
        posicion += 1
        limite -= 1
    return superposicion

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    cadena_1 = str(input("Ingrese cadena 1: "))
    cadena_2 = str(input("Ingrese cadena 2: "))
    superposicion = compara_cadenas(cadena_1, cadena_2)
    if superposicion == None:
        print("No hay superposicion")
    else:
        print(f"La superposicion inicia en: {superposicion}")

if __name__ == "__main__":
    principal()
