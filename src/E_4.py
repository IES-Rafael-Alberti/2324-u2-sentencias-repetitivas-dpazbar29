#2.2.4
'''
Escribir un programa que pida al usuario un número entero positivo
muestre por pantalla la cuenta atrás desde ese número hasta cero
separados por comas
'''

def cuentaAtras(numero1):
    cuenta_atras = [str(i) for i in range(numero1, -1, -1)]
    StrResultado = ", ".join(cuenta_atras)

    return StrResultado

def mensajeSalida4(sucesion_numeros):
     return "Cuenta atrás: " + str(sucesion_numeros)


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
    sucesion_numeros = cuentaAtras(numero1)
    mensaje_salida = mensajeSalida4(sucesion_numeros)

    #devolvemos
    print(mensaje_salida)
