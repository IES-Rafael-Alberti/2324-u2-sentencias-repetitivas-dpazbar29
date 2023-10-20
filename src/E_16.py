#2.2.16
'''
Lee numeros positivos hasta que se introduzca 0
muestra cual ha sido el numero mayor introducido
'''

def comparativaNumeros():
    maximo = 0
    while True:
        numero = int(input("Introduce un número entero positivo (0 para terminar): "))
        if numero == 0:
            break
        if numero > maximo:
            maximo = numero
    return maximo

def mensajeSalida16(resultado_comparativa):
    return "El numero mas alto ingresado es: " + str(resultado_comparativa)

if __name__ == "__main__":

    #leemos

    #proceso
    resultado_comparativa = comparativaNumeros()
    mensaje = mensajeSalida16(resultado_comparativa)

    #devolvemos
    print(mensaje)