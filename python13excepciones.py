import sys
#DECLARAMOS UN METODO QUE LANZARA UNA EXCEPCION O NO...
def controlErrores():
    try:
        numero1 = int(input("Introduzca dividendo: "))
        numero2 = int(input("Introduzca divisor: "))
        resultado = numero1 / numero2
        print(f"El resultado de la división es {resultado}")
    except:
        print(f"Error inesperado: {sys.exc_info()}")

print("Control de excepciones")
controlErrores()
print("Fin de programa")
