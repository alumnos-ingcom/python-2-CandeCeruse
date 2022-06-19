################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Estadísticas

Implementar una función que obtenga los máximos, mínimos y promedio
de una secuencia con números, retornando los valores como una tuple.

Sin utilizar lazos for o las funciones integradas del lenguaje que procesan secuencias.
"""
# Reemplazar por las funciones del ejercicio
def ingresa_numeros():
    """
    Esta funcion sirve para ingresar 10 numeros enteros
    y guardarlos en una tupla
    """
    limite = 10
    numeros = []
    while limite > 0:
        numero = int(input("Ingrese numero: "))
        numeros.append(numero)
        limite -= 1
    numeros = tuple(numeros)
    return numeros

def busca_maximo(cadena):
    """
    Esta funcion busca el maximo de la tupla de numeros
    """
    limite = len(cadena)
    posicion = -len(cadena)
    maximo = cadena[posicion]
    while limite > 0:
        if maximo < cadena[posicion]:
            maximo = cadena[posicion]
        else:
            pass
        limite -= 1
        posicion += 1
    return maximo

def busca_minimo(cadena):
    """
    Esta funcion busca el minimo de la tupla de numeros
    """
    limite = len(cadena)
    posicion = -len(cadena)
    minimo = cadena[posicion]
    while limite > 0:
        if minimo > cadena[posicion]:
            minimo = cadena[posicion]
        else:
            pass
        limite -= 1
        posicion += 1
    return minimo

def promedia(cadena):
    """
    Esta funcion busca el promedio de los numeros
    de la cadena
    """
    limite = len(cadena)
    sumados = 0
    posicion = -len(cadena)
    while limite > 0:
        sumados = sumados + cadena[posicion]
        limite -= 1
        posicion += 1
    promedio = float(sumados / len(cadena))
    return promedio

def crea_tupla(maximo, minimo, promedio):
    """
    Esta funcion devuelve una tupla para que
    la salida del programa sea utilizable.
    """
    resultado = [maximo, minimo, promedio]
    resultado = tuple(resultado)
    return resultado

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numeros = ingresa_numeros()
    maximo = busca_maximo(numeros)
    minimo = busca_minimo(numeros)
    promedio = promedia(numeros)
    resultado = crea_tupla(maximo, minimo, promedio)
    
    print(f"Maximo: {maximo}")
    print(f"Minimo: {minimo}")
    print(f"Promedio: {promedio}")
    print(resultado)

if __name__ == "__main__":
    principal()