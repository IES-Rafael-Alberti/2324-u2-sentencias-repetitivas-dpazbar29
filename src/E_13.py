#2.2.13
'''
muestra todo lo que escriba el usuario hasta que escriba salir
'''
def ecoUsuario():
    while True:
        entrada = input("Introduce algo (escribe 'salir' para terminar): ")
        if entrada.lower() == 'salir':
            break
        print(entrada)

if __name__ == "__main__":

    #leemos

    #proceso

    #devolvemos
    ecoUsuario()
