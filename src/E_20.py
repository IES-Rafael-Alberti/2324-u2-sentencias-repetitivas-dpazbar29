#2.2.20
'''
Solicitar al usuario el ingreso de una frase y de una letra
(que puede o no estar en la frase)
Recorrer la frase, carácter a carácter, comparando con la letra buscada.
Si el carácter no coincide, indicar que no hay coincidencia en esa posición 
(imprimiendo la posición) y continuar
Si se encuentra una coincidencia, indicar en qué posición se encontró y final.
'''

def buscar_letra_en_frase(frase, letra):
    for i, caracter in enumerate(frase):
        if caracter == letra:
            print ("Se encontró la letra '" + str(letra) + "' en la posición " + str(i))
        else:
            print ("No hay coincidencia en la posición " + str(i))

if __name__ == "__main__":

    #leemos
    frase = input("Introduce una frase: ")
    letra = input("Introduce una letra: ")

    #proceso
    buscar = buscar_letra_en_frase(frase, letra)
