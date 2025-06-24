print("Ejemplo de diccionarios")
#CREAMOS EL DICCIONARIO DE PROVINCIAS
provincias = dict()
provincias = {
    924 : "Badajoz",
    956:  "Cádiz",
    958 : "Granada",
    959 : "Huelva",
    91 : "Madrid",
    95 : "Málaga",
    968 : "Murcia"
}
#AÑADIMOS UNA NUEVA PROVINCIA, SI LA KEY NO EXISTE LO INSERTA
provincias.setdefault(976, "Zaragoza")
#QUE SUCEDE SI EXISTE????
provincias.setdefault(968, "Albacete")
provincias.pop(958)
print(f"Número de provincias: {len(provincias)}")
for key, value in provincias.items():
    print(f"key: {key}, valor: {value}")
print("--------------KEYS------------------")
for key in provincias.keys():
    print(f"key: {key}")
print("--------------VALUES------------------")
for value in provincias.values():
    print(f"Valor: {value}")    