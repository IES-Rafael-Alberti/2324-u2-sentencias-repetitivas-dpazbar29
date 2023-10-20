#2.2.14
'''
lee numeros enteros hasta ingresar 0
muestra la suma de todos los numeros introducidos
'''
def sumatoriaNumeros():
    suma = 0
    while True:
        numero = int(input("Introduce un número entero (0 para terminar): "))
        if numero == 0:
            break
        suma += numero
    return suma

def mensajeSalida14(resultado_suma):
    return "La sumatoria de todos los números ingresados es: " + str(resultado_suma)


if __name__ == "__main__":

    #leemos

    #proceso
    resultado_suma = sumatoriaNumeros()
    mensaje = mensajeSalida14(resultado_suma)

    #devolvemos
    print(mensaje)
