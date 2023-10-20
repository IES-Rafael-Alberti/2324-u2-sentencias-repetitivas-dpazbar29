#2.2.24
'''
Escribir un programa que solicite el ingreso de una cantidad de números > 1
finalizando cuando se reciba un cero
Imprimir la cantidad de números primos ingresados.
'''

def esPrimo(numero):
    if numero == 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

if __name__ == "__main__":
    
    numeros_primos = 0

    while True:
        #leemos
        num = int(input("Ingrese un número mayor que 1 (0 para terminar): "))
        
        if num == 0:
            break
        if num > 1 and esPrimo(num):
            numeros_primos += 1

    #devolvemos
    print("La cantidad de números primos ingresados es: " + str(numeros_primos))