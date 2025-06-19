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
#-------------------------------------------------------------
#CODIGO PRINCIPAL DE NUESTRO PROGRAMA MAIN
print("Ejemplo métodos")
saludar("Paco")
despedirse("Paco", "Juernes")
#LLAMADA LOS METODOS
primerMetodo()
segundoMetodo()
primerMetodo()
print("Fin de programa")