print("Sumar números de textos")
textoNumeros = input("Introduzca un texto numerico")
suma = 0
# Realizamos un bucle para recorrer cada letra del texto
for i in range(len(textoNumeros)):
    #ALMACENAMOS CADA LETRA DE CADA POSICION
    letra = textoNumeros[i]
    # EXTRAEMOS CADA LETRA Y LA CONVERTIMOS A int
    numero = int(letra)
    suma = suma + numero
print(f"La suma de {textoNumeros} es: {suma}")
print("Fin de programa")