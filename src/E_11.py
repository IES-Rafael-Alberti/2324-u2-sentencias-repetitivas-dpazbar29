#2.2.11
'''
Pide una palabra y muestra una a una las letras
'''

def mostrarLetras(palabra):

    resultado = []
    
    for i in range(len(palabra)-1, -1, -1):
        
        resultado.append(palabra[i])
        strResultado = " ".join(resultado)
    return strResultado


def mensajeSalida11(letras):
    return "Resultado: " + str(letras)


if __name__ == "__main__":

    #leemos
    palabra = str(input("Introduzca la palabra a dividir: "))

    #proceso
    letras = mostrarLetras(palabra)
    mensaje_salida = mensajeSalida11(letras)

    #devolvemos
    print(mensaje_salida)