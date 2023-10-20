#2.2.17
'''
Leer un número entero positivo desde teclado
imprimir la suma de los dígitos que lo componen.

'''

def sumaDigitos(numero:int) -> int:
    suma = 0
    while numero > 0:
        #obtenemos el último dígito
        digito = numero % 10
        suma += digito
        #obtenemos el prmier dígito
        numero //= 10
    return suma

def mensajeSalida17(numero:int,resultado:int) -> str:
    return "La suma de los dígitos de " + str(numero)  + " es: " + str(resultado)



if __name__ == "__main__":

    #leemos
    numero = int(input("Introduce un número entero positivo: "))

    #proceso
    resultado = sumaDigitos(numero)
    mensaje = mensajeSalida17(numero,resultado)

    #devolvemos
    print(mensaje)