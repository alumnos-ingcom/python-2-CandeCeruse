################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Implementar una funcion que codifique un texto rotandolo una cantidad de posiciones ajustable.

Implementar la funcion que decodifique el texto rotado una cantidad de posiciones ajustable.
"""
def cifrado_del_cesar(texto, cantidad):
    i = 0
    texto_original = texto
    abc = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R',
           'S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k',
           'l','m','n','ñ','o','p','q','r','s','t','u','w','x','y','z','0','1','2','3',
           '4','5','6','7','8','9')
    abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuwxyz0123456789"
    while i < len(texto):
        texto.replace(texto[i], ord(texto[i]))
        i += 1
    
    return texto

def traduce_a_unicode(texto, cantidad):
    limite = len(texto)
    i = 0
    unicode = []
    while limite > 0:
        caracter = ord(texto[i])
        caracter_encriptado = caracter + cantidad
        unicode.append(caracter_encriptado)
        limite -= 1
        i += 1
    return unicode

def unicode_a_encriptado(texto):
    limite = len(texto)
    i = 0
    encriptado = []
    salida = ""
    while limite > 0:
        caracter = chr(texto[i])
        encriptado.append(caracter)
        limite -= 1
        i += 1
    print(salida.join(encriptado))
    return salida

def principal():
    """
    Valor de entrada = str
    Valor de salida = str
    """
    texto = input("Introduzca un texto a cifrar: ")
    cantidad = int(input("Introduzca una cantidad de carácteres para cifrar: "))
    #final = cifrado_del_cesar(texto, cantidad)
    #print(final)
    unicode = traduce_a_unicode(texto, cantidad)
    print(unicode)
    print(unicode_a_encriptado(unicode))

if __name__ == "__main__":
    principal()