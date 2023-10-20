#2.2.7
'''
Muestra por pantalla la tabla de multiplicar de cualquier numero
'''

def tabla(numero):
    resultado = []
    cont = 0
    while cont <= 10 - 1:
        cont += 1
        resultado.append( str(numero) + " * " + str(cont) + " = " + str(numero * cont))
        strResultado = "\n".join(resultado)
    return strResultado


if __name__ == "__main__":

    #leemos
    numero = int(input("Introduca el numero al que haremos la tabla: "))

    #proceso
    resultado_final = tabla(numero)

    #devolvemos
    print(resultado_final)