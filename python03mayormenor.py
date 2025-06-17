print("Operadores relacionales")
num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
num3 = int(input("Número 3: "))
mayor = 0
menor = 0
intermedio = 0
if (num1 >= num2 and num1 >= num3):
    mayor = num1
elif (num2 >= num1 and num2 >= num3):
    mayor = num2
else:
    mayor = num3
if (num1 <= num2 and num1 <= num3):
    menor = num1
elif (num2 <= num1 and num2 <= num3):
    menor = num2
else:
    menor = num3
suma = num1 + num2 + num3
intermedio = suma - mayor - menor
print(f"Mayor: {mayor}, Menor: {menor}, Intermedio: {intermedio}")
print("Fin de programa")