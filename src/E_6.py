#2.2.6
'''
Pide un numero entero
Muestra un triangulo rectangulo con la altura del numero introducido
def imprimirTriangulo(altura):

    resultado = []
    contador = altura
    
    while contador >= altura:
        contador -= 1
        resultado.append("*") 
        StrResultado = " ".join(resultado)

    return StrResultado



if __name__ == "__main__":

    #leemos
    altura = int(input("Introduce la altura del triángulo: "))

    #proceso

    #devolvemos
    print(imprimirTriangulo(altura))
'''
