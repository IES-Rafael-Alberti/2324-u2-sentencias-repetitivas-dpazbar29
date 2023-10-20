#2.2.18
'''
solicita numeros e imprime la suma de los digitos que lo componen
se corta si ingresas -1
mostrar cuantos de los numeros son pares
'''

def sumaDigitos18(numero):
    suma = 0
    while numero > 0:
        digito = numero % 10
        suma += digito
        numero //= 10
    return suma

def contarPares(lista):
    contador = 0
    for numero in lista:
        if numero % 2 == 0:
            contador += 1
    return contador

numeros_ingresados = []

def mensajeSalida18Suma(numero,suma):
    return "La suma de los dígitos de " + str(numero) + " es: " + str(suma)

def mensajeSalida18Pares(cantidad_pares):
    return "La cantidad de números pares ingresados fue: " + str(cantidad_pares)


while True:
    numero = int(input("Introduce un número entero positivo (-1 para terminar): "))
    if numero == -1:
        break
    suma = sumaDigitos18(numero)
    
    salida_suma = mensajeSalida18Suma(numero,suma)
    print(salida_suma)

    numeros_ingresados.append(suma)

cantidad_pares = contarPares(numeros_ingresados)

salida_pares = mensajeSalida18Pares(cantidad_pares)
print(salida_pares)