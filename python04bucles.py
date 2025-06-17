print("Ejemplos y sintaxis de bucles")
#REALIZAMOS EL TIPICO DE MOSTRAR LOS NUMEROS PARES ENTRE UN RANGO
for i in range(2, 20):
    #PREGUNTAMOS SI UN NUMERO ES PAR
    #UTILIZAMOS EL OPERADOR DEL RESTO: %
    if (i % 2 == 0):
        print(f"Par: {i}")
print("----------Collatz----------------")
numero = int(input("Introduzca numero: "))
while (numero != 1):
    if (numero % 2 == 0):
        numero = int(numero / 2)
    else:
        numero = numero * 3 + 1
    print(numero)
print("Fin de programa")