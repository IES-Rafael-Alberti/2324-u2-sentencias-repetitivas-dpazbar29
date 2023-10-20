#2.2.2
'''
Escribir un programa que pregunte al usuario su edad
muestre por pantalla todos los años que ha cumplido
(desde 1 hasta su edad).
'''
def secuencia(edad):
    resultado=[]
    contador = 1
    
    while contador <= edad:
        resultado.append(contador)
        contador += 1
        
    return str(resultado)

def mensajeSalida2(bucle):
    return "Resultado: " + str(bucle)


if __name__ == "__main__":

    #leemos
    edad = int(input("Introduzca su edad: "))

    #proceso
    bucle = secuencia(edad)
    mensaje_salida = mensajeSalida2(bucle)

    #devolvemos
    print(mensaje_salida)