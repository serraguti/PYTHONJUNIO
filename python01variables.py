print("Ejemplo de variables")
numero = 19
texto = "Hola mundo"
#Comentarios en Python
# Para comentar y descomentar código de una sola vez en VS Code.ç
# Comentar:  CONTROL + K + C
# Descomentar: CONTROL + K + U
print(numero)
print(texto)
# Tenemos la posibilidad de concatenar +: Verifica el tipado
# print("numero " + numero) # error
# Con coma no verifica tipado
print("numero ", numero)
print("texto " + texto)
#print f nos permite concatenar múltiples variables en un String sin 
#importar el tipado: Cada variable irá entre llaves {variable}
print(f"El texto es {texto} y el numero es {numero}")
#Dentro de las variables tenemos funciones de conversión lo que permiten convertir 
#entre un tipo y otro, por ejemplo:
#str(variable): Convierte un valor a string
#float(variable): Convierte variable a tipo decimal
#int(variable): Convierte variable a entero
print("numero " + str(numero))