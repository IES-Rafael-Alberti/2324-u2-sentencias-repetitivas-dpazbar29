#2.2.10
'''
Pide un numero entero y muestra si es primo o no
'''

def primo(numero):

    if numero == 2:
        return False
    for i in range(2,numero):
        if numero % i == 0:
            return False 
    return True

if __name__ == "__main__":

    #leemos
    numero = int(input("Introduzca el numero a saber si es o no primo: "))

    #proceso
    prim = primo(numero)
    
    #devolvemos
    print(prim)