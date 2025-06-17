print("Condicionales Python")
print("Introduzca un número")
#input() siempre devuelve STRING, no importa si el string es una 
#fecha, número o un decimal
numero = int(input())
if (numero > 0):
    print("Positivo")
elif (numero == 0):
    print("Cero")
else:
    print("Negativo")
print("Fin de programa")