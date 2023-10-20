#2.2.12
'''
pregunta una frase y una letra y muestra el numero de veces que aparece en ella
'''

def contarLetra(frase,letra):
    contador = 0
    for i in frase:
        if i == letra:
            contador += 1
    return contador

def mensajeSalida12(letra,cont_letra):
    return "La letra " + str(letra) + " aparece " + str(cont_letra) + " veces"

if __name__ == "__main__":

    #leemos
    frase = input("Introduce una frase: ").lower()
    letra = input("Introduce una letra de la frase para saber su numero de apariciones: ")

    #proceso
    cont_letra = contarLetra(frase,letra)
    mensaje = mensajeSalida12(letra,cont_letra)

    #devolvemos
    print(mensaje)