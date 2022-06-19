################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Implementar una funcion que codifique un texto rotandolo una cantidad de posiciones ajustable.
"""
def unicode_a_texto(texto, unicode):
    """
    Función que transforma a un string el unicode ingresado.
    """
    limite = len(texto)
    i = 0
    encriptado = []
    salida = ""
    while limite > 0:
        caracter = chr(unicode[i])
        encriptado.append(caracter)
        limite -= 1
        i += 1
    salida = salida.join(encriptado)
    return salida

def encripta(texto, rotacion):
    """
    Esta funcion toma el texto y rotacion ingresados para encriptar. Luego
    toma el primer caracter de la cadena y revisa si es mayúscula, minúscula o un dígito.
    Dependiendo de lo que sea, establece un minimo que esta dado por el primer caracter
    de unicode del grupo al que pertenece. Así si la rotación es mayor a los caracteres
    disponibles vuelve al inicio. Consecutivamente convierte los caracteres a la rotacion
    indicada.
    Devuelve una lista con el unicode encriptado del mensaje.
    """
    i = 0
    rotacion_original = rotacion
    limite = len(texto)
    unicode = []
    while limite > 0:
        caracter = ord(texto[i])
        if texto[i].isupper():
            minimo = 65
            while caracter <= 90 and rotacion > 0:
                caracter += 1
                rotacion -= 1
                if caracter > 90:
                    caracter = minimo
                else:
                    continue
        elif texto[i].islower():
            minimo = 97
            while caracter <= 122 and rotacion > 0:
                caracter += 1
                rotacion -= 1
                if caracter > 122:
                    caracter = minimo
                else:
                    continue
        elif texto[i].isdigit():
            minimo = 48
            while caracter <= 57 and rotacion > 0:
                caracter += 1
                rotacion -= 1
                if caracter > 57:
                    caracter = minimo
                else:
                    continue
        else:
            pass
        limite -= 1
        i += 1
        rotacion = rotacion_original
        unicode.append(caracter)
    return unicode

def desencripta(encriptado, rotacion):
    """
    Función que desencripta el mensaje en encriptado como str por el usuario
    """
    rotacion_original = rotacion
    limite = len(encriptado)
    i = 0
    desencriptado = []
    while limite > 0:
        caracter = ord(encriptado[i])
        if encriptado[i].isupper():
            maximo = 90
            while caracter >= 65 and rotacion > 0:
                caracter -= 1
                rotacion -= 1
                if caracter < 65:
                    caracter = maximo
                else:
                    continue
        elif encriptado[i].islower():
            maximo = 122
            while caracter >= 97 and rotacion > 0:
                caracter -= 1
                rotacion -= 1
                if caracter < 97:
                    caracter = maximo
                else:
                    continue
        elif encriptado[i].isdigit():
            maximo = 57
            while caracter >= 48 and rotacion > 0:
                caracter -= 1
                rotacion -= 1
                if caracter < 48:
                    caracter = maximo
                else:
                    continue
        else:
            pass
        limite -= 1
        i += 1
        rotacion = rotacion_original
        desencriptado.append(caracter)
    return desencriptado

def principal():
    """
    Valor de entrada = str
    Valor de salida = str
    """
    texto = input("Introduzca un texto a cifrar: ")
    rotacion = int(input("Introduzca una rotacion de carácteres para cifrar: "))
    unicode_encriptado = encripta(texto, rotacion)
    print(unicode_encriptado)
    encriptado = unicode_a_texto(texto, unicode_encriptado)
    print(f'Encriptado: {encriptado}')
    unicode_desencriptado = desencripta(encriptado, rotacion)
    print(unicode_desencriptado)
    desencriptado_final = unicode_a_texto(texto, unicode_desencriptado)
    print(f'Desencriptado: {desencriptado_final}')

if __name__ == "__main__":
    principal()