#2.2.23
'''
Crear un programa que permita al usuario ingresar títulos de libros por teclado
finalizando el ingreso al leerse el string “*”
Cada vez que el usuario ingrese un string de longitud 1
que contenga sólo una barra (“/”) se considera que termina una línea
Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) tiene 
(en todos los títulos de libros que componen en esa línea)
Finalmente, informar cuántas líneas completas se ingresaron.
'''

def contarDigitos(cadena):
    contador = 0
    for caracter in cadena:
        if caracter.isdigit():
            contador += 1
    return contador


if __name__ == "__main__":

    lineas_completas = 0
    titulo_libros = ""
    
    while True:
        entrada = input("Ingrese un título de libro (ingrese '*' para finalizar): ")
        if entrada == "*":
            break
        if "/" in entrada and len(entrada) == 1:
            lineas_completas += 1
            digitos_en_linea = contarDigitos(titulo_libros)
            print("En la línea completa se ingresaron " + str(digitos_en_linea) + " dígitos numéricos.")
            titulo_libros = ""
        else:
            titulo_libros += entrada

    print("Se ingresaron un total de " + str(lineas_completas) +" líneas completas.")