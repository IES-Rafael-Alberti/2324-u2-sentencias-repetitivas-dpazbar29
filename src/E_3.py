#2.2.3
'''
Escribir un programa que pida al usuario un número entero positivo
muestre por pantalla todos los números impares
desde 1 hasta ese número separados por comas.
'''

def numerosImpares(numero1):
    impares = [str(i) for i in range(1, numero1 + 1) if i % 2 != 0]
    StrResultado = ", ".join(impares)

    return StrResultado

def mensajeSalida3(obtencion):
     return "Numeros impares: " + str(obtencion)

if __name__ == "__main__":

    #leemos
    while True:
            try:
                numero1  = int(input("Introduzca un numero positivo y entero: "))
            except ValueError:
                print("Ha de ser positivo y entero")
                continue
            break

    #proceso
    obtencion = numerosImpares(numero1)
    mensaje_salida = mensajeSalida3(obtencion)

    #devolvemos
    print(mensaje_salida)