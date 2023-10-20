#2.2.19
'''
Mostrar un menú con tres opciones:
1- comenzar programa
2- imprimir listado
3-finalizar programa. 
A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3)
Si elige una opción incorrecta, informarle del error.
El menú se debe volver a mostrar luego de ejecutada cada opción
permitiendo volver a elegir.
Si elige las opciones 1 ó 2 se imprimirá un texto.
Si elige la opción 3, se interrumpirá la impresión del menú y el programa acaba
'''

def menu():
    return "Menú: \n1-Comenzar programa\n2-Imprimir listado\n3-Finalizar programa\n"

def accion(opcion):
    while True:
        if opcion == '1':
            return("El programa ha comenzado.")
        elif opcion == '2':
            imprimirListado()
        elif opcion == '3':
            return("El programa ha finalizado.")
            break
        else:
            return("Opción incorrecta. Por favor, seleccione una opción válida.")

        print("\n")

def imprimirListado():
    print("Este es el listado.")

if __name__ == "__main__":
    #devolvemos
    while True:
        print(menu())

        #leemos
        opcion = input("Seleccione una opción: ")

        #proceso
        act = accion(opcion)
        
