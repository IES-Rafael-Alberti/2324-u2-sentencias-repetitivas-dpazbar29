#2.2.21
'''
Crear un programa que permita al usuario ingresar los montos de las compras
 (se desconoce la cantidad de datos que cargará)
 (la cual puede cambiar en cada ejecución)
 cortando el ingreso de datos cuando el usuario ingrese el monto 0.
 Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese
un nuevo monto.
Al finalizar, informar el total a pagar teniendo que cuenta que
si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.
'''

def calcularPago(compras):
    total = sum(compras)
    if total > 1000:
        descuento = total * 0.1
        total -= descuento
    return total

def mensajeSalida21(total_pago):
    return "El total a pagar es: " + str(total_pago)

compras = []

if __name__ == "__main__":
    
    #proceso
    while True:
        
        #leemos
        monto = float(input("Ingrese el monto de la compra (0 para terminar): "))
        
        #proceso
        if monto == 0:
            break
        elif monto < 0:
            print("Monto inválido. Ingrese un monto válido.")
            continue
        else:
            compras.append(monto)

    total_pago = calcularPago(compras)
    mensaje = mensajeSalida21(total_pago)

    #devolvemos
    print(mensaje)
