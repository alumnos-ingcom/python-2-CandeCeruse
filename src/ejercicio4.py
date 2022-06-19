################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
4. Fibonacci

La sucesión de Fibonacci es una sucesión infinita donde cada elemento
es la suma de los dos anteriores. En la misma, los dos primeros términos
son 1. (En algunos lugares se toma el primer término en 0 y el segundo en 1)
Implementar una función que permita obtener el n-esimo termino de la sucesión
de Fibonacci. Siendo este número un entero positivo mayor a 2.
"""
# Reemplazar por las funciones del ejercicio
def fibonacci(limite):
    reingreso = 2
    while limite < 2 and reingreso > 0:
        print("El termino debe ser mayor que 2")
        limite = int(input("Ingrese de nuevo: "))
        reingreso -= 1
    if limite > 2:
        termino_anterior = 1
        termino_siguiente = 1
        while limite > 0 and reingreso > 0:
            suma = termino_anterior + termino_siguiente
            termino_anterior = termino_siguiente
            termino_siguiente = suma
            limite -= 1
    else:
        print("Siga participando")
    return suma

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    limite = int(input("Ingrese termino de la sucesion que quiere averiguar: "))
    resultado = fibonacci(limite)
    print(f"Termino nro {limite} de la sucesion es {resultado}")

if __name__ == "__main__":
    principal()
