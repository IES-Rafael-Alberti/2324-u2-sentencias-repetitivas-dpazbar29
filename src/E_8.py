#2.2.8
'''
Escribir un programa que pida al usuario un número entero
muestre por pantalla un triángulo rectángulo como el de más abajo
'''

def triangulo(num):
    resultado = []
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            resultado.append(str(j))
        strResultado = " ".join(resultado)
    return strResultado


if __name__ == "__main__":

    #leemos
    num = int(input("Introduce la altura del triángulo: "))

    #proceso
    triangulo = triangulo(num)

    #devolvemos
    print(triangulo(num))