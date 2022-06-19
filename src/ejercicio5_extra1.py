################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
5. Corchetes balanceados

Implementar una función que determine si una cadena con corchetes está balanceada.

Es decir, si cada corchete que abre, tiene su par que cierra. El resultado
debe ser un valor lógico indicando si esta o no balanceado.
"""
# Reemplazar por las funciones del ejercicio
def determina_balance(cadena, caracter_apertura, caracter_cierre):
    limite = len(cadena)
    corchete_apertura = 0
    corchete_cierre = 0
    posicion = 0
    primer_apertura = cadena.find(caracter_apertura)
    primer_cierre = cadena.find(caracter_cierre)
    posicion_apertura = 0
    posicion_cierre = 0
    
    if cadena == '':
        resultado = True
    else:
        if primer_cierre < primer_apertura:
            resultado = False
        else:
            while limite > 0:
                apertura = cadena.find(caracter_apertura, posicion_apertura)
                cierre = cadena.find(caracter_cierre, posicion_cierre)
                if apertura <= cierre:
                    if cadena[posicion] == caracter_apertura:
                        corchete_apertura += 1
                    elif cadena[posicion] == caracter_cierre:
                        corchete_cierre += 1
                    posicion += 1
                    limite -= 1
                    posicion_apertura = posicion_cierre
                    posicion_cierre += 1
                    if corchete_apertura == corchete_cierre:
                        resultado = True
                    else:
                        resultado = False
                else:
                    resultado = False
                    break
    return resultado

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    cadena = str(input("Ingrese cadena: "))
    caracter_apertura = str(input("Ingrese caracter de apertura: "))
    caracter_cierre = str(input("Ingrese caracter de cierre: "))
    resultado = determina_balance(cadena, caracter_apertura, caracter_cierre)
    print(resultado)
if __name__ == "__main__":
    principal()
