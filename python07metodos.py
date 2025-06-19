#Comenta: control + k + c
#Descomentar: control + k + u
# EN UN PROGRAMA LOS METODOS DEBEN 
# ESTAR ANTES DE LA LLAMADA, POR LO QUE 
# SE SUELEN DECLARAR AL INICIO
def primerMetodo():
    #ESTE CODIGO JAMAS SE EJECUTARA 
    # SIN SER LLAMADO DE FORMA EXPLICITA
    print("Ejecutando metodo 1")
def segundoMetodo():
    print("Ejecutando metodo 2")
def saludar(nombre):
    print("Bienvenido/a a Python ", nombre)
def despedirse(nombre, dia):
    print(f"Hasta luego {nombre} en el dia {dia}")
#METODO DE ACCION
def mostrarMenu():
    print("Seleccione una opción")
    print("1.- Convertir a mayúsculas")
    print("2.- Convertir a minúsculas")
#METODOS CON RETURN. LA SINTAXIS ES LA MISMA
def convertirMayusculas(texto):
    return texto.upper()
def convertirMinusculas(texto):
    return texto.lower()
#-------------------------------------------------------------
#CODIGO PRINCIPAL DE NUESTRO PROGRAMA MAIN
print("Ejemplo métodos")
mostrarMenu()
#LOS METODOS QUE DEVUELVEN VALOR DEBEN ALMACENAR EL 
#VALOR DEVUELTO EN ALGUN SITIO/VARIABLE
mayus = convertirMayusculas("curso de python")
print(mayus)
minus = convertirMinusculas("CURSo dE PyThon")
print(minus)
# saludar("Paco")
# despedirse("Paco", "Juernes")
# #LLAMADA LOS METODOS
# primerMetodo()
# segundoMetodo()
# primerMetodo()
print("Fin de programa")