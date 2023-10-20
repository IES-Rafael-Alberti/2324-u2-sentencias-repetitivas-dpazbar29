#2.2.1
'''
Pide al usuario una palabra y muestrala 10 veces por pantalla
'''
def repeticion(palabra):
    resultado=[]
    contador = 0
    
    while contador < 10:
        resultado.append(palabra)
        contador += 1
        StrResultado = " ".join(resultado)
    return str(StrResultado)

def mensajeSalida1(bucle):
    return "Resultado: " + str(bucle)

if __name__ == "__main__":
    
    #leemos
    palabra = input("Introduce una palabra a repetir 10 veces: ")

    #proceso    
    bucle = repeticion(palabra)
    mensaje_salida = mensajeSalida1(bucle)

    #devolvemos
    print(mensaje_salida)
