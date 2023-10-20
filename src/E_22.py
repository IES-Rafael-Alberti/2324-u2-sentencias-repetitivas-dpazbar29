#2.2.22
'''
Crear un programa que solicite el ingreso de números enteros positivos
hasta que el usuario ingrese el 0.
Por cada número, informar cuántos dígitos pares y cuántos impares tiene
Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos
'''
def contarParImp(numero):
    pares = 0
    impares = 0
    while numero > 0:
        digito = numero % 10
        if digito % 2 == 0:
            pares += 1
        else:
            impares += 1
        numero //= 10
    return pares, impares

total_pares = 0
total_impares = 0


while True:
    numero = int(input("Ingrese un número entero positivo (0 para terminar): "))
    if numero == 0:
        break
    elif numero < 0:
        print("Número inválido. Ingrese un número positivo.")
        continue
    else:
        pares, impares = contarParImp(numero)
        total_pares += pares
        total_impares += impares
        print("El número" + str(numero) + "tiene" + str(pares) + "dígitos pares y " + str(impares) + "dígitos impares.")

print("En total, se leyeron " + str(total_pares) + " dígitos pares y " + str(total_impares) + " dígitos impares.")