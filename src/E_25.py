#2.2.25
'''
Solicitar al usuario que ingrese una frase
luego informar cuál fue la palabra más larga
(en caso de haber más de una, mostrar la primera) y cuántas palabras había
Precondición: se tomará como separador de palabras al carácter “ “ (espacio)
'''
def encontrarPalabra(frase):
    palabras = frase.split()
    max_longitud = 0
    palabra_larga = ""
    for palabra in palabras:
        if len(palabra) > max_longitud:
            max_longitud = len(palabra)
            palabra_larga = palabra
    return palabra_larga

def palabrasTotales(frase):
    return len(frase.split())

def mensajeSalida25(palabra_larga,palabras_totales):
    return "La palabra mas larga es: " + str(palabra_larga) + "\nEl número total de palabras es: " + str(palabras_totales)


if __name__ == "__main__":

    #leemos
    frase = input("Ingrese una frase: ")

    #proceso
    palabra_larga = encontrarPalabra(frase)
    palabras_totales = palabrasTotales(frase) 
    mensaje = mensajeSalida25(palabra_larga,palabras_totales)

    #devolvemos
    print(mensaje)
