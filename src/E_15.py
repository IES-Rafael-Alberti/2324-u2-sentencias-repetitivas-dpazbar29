#2.2.15
'''
Lee numeros enteros hasta que se de el 0
muestra la suma de los numeros positivos
'''

def sumatoriaNumeros():
    suma = 0
    while True:
        numero = int(input("Introduce un número entero (0 para terminar): "))
        if numero == 0:
            break
        if numero > 0:
            suma += numero
    return suma

def mensajeSalida15(resultado_suma):
    return "La sumatoria de todos los números ingresados es: " + str(resultado_suma)


if __name__ == "__main__":

    #leemos

    #proceso
    resultado_suma = sumatoriaNumeros()
    mensaje = mensajeSalida15(resultado_suma)

    #devolvemos
    print(mensaje)
