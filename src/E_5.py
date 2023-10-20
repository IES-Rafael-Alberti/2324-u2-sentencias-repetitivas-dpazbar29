#2.2.5
'''
Pregunta una cantidad a invertir,el interés anual y el numero de años
Muestra el capital obtenido en la inversión a cada año que pasa
'''

def pasarPorcentaje(interes_anual:float) -> float:
    return float(interes_anual / 100)

def calculo(cantidad_invertir:float,interes_decimal:float,numero_años:int) -> float:
    
    cont = 0
    while cont <= numero_años:
        cantidad_invertir *= 1 + interes_decimal
        cont += 1
        return cantidad_invertir

def mensajeSalida5(capital:float) -> str:
    return "El capital obtenido es: " + str(capital)


if __name__ == "__main__":

    #leemos
    cantidad_invertir = float(input("Introduzca la cantidad que quiere invertir: "))
    interes_anual = float(input("Introduzca el interés anual: "))
    numero_años = int(input("Introduzca el número de años: "))

    #proceso
    interes_decimal = pasarPorcentaje(interes_anual)
    capital = calculo(cantidad_invertir,interes_decimal,numero_años)
    mensaje_salida = mensajeSalida5(capital)

    #devolvemos
    print(mensajeSalida5(capital))