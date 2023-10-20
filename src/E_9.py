#2.2.9
'''
Almacena la cadena "contraseña" en una variable
pregunta por la contraseña hasta que sea correcta
'''

def comprobacion(contraseña):
    while contraseña != "contraseña":
        print("La contraseña no es correcta")
        contraseña = (input("Introduce la contraseña: "))
    return "¡La contraseña es correcta!"



if __name__ == "__main__":

    #leemos
    contraseña = (input("Introduce la contraseña: "))

    #proceso
    mensaje = comprobacion(contraseña)

    #devolvemos
    print(mensaje)