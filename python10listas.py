print("Ejemplo de listas")
#la declaracion de una lista puede ser ya 
#con los objetos o sin objetos
listaNumeros = [12, 88, 11, 21, 33, 22, 31, 2]
#ORDEN ASCENDENTE
#TODOS LOS METODOS DE LA LISTA MODIFICAN EL OBJETO
#ASCENDENTE
#listaNumeros.sort()
#Tenemos una opción para indicar que el orden sera DESCENDENTE
listaNumeros.sort(reverse=True)
#REALIZAMOS UN BUCLE PARA DIBUJAR LOS DATOS
# for i in range(len(listaNumeros)):
#     print(listaNumeros[i])
#CREAMOS UNA NUEVA LISTA DE NOMBRES
listaNombres = ["Adrian", "Lucia", "Antonia", "Diana", "Carlos", "Adrian"]
listaNombres.append("Carlos")
listaNombres.insert(17, "El nuevo")
#PROBAMOS EL METODO remove()
#Remove, si no encuentra el nombre, dará Excepción
#listaNombres.remove("Carlitos")
#Probamos con pop a ver que sucede
#Al eliminar, tendremos excepción si no existe
#listaNombres.pop(17)
print(f"Longitud: {len(listaNombres)}")
#DIBUJAMOS TODOS LOS NOMBRES
for i in range(len(listaNombres)):
    nombre = listaNombres[i]
    listaNombres.append("Paco")
    print(f"{i}: {nombre}")
# for nombre in listaNombres:
#     listaNombres.append("Paco")
#     print(nombre)
