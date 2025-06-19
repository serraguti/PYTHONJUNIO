print("Ejemplo de tuplas")
productos = ("Leche", "Cacao", "Avellanas", "Azucar")
#No podemos modificar una Tupla
productos[0] = "Leche desnatada"
print(f"Elementos de tupla {len(productos)}")
#PODEMOS UTILIZAR BUCLES DE REFERENCIA
for prod in productos:
    print(prod)