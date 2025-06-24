from models.persona import Persona

print("Probando la clase Persona de POO")
#CREAMOS UNA INSTANCIA DE PERSONA
personaje = Persona()
personaje.nombre = "Sheldon"
personaje.apellidos = "Cooper"
print(personaje.getNombreCompleto()) #normal
print(personaje.getNombreCompleto(22)) #reves
# print(personaje.getNombreCompleto(33,33))
print(f"Nacionalidad: {personaje.pais}, Edad: {personaje.edad}")
#ENCAPSULACION
print(personaje.getPrivateDni())
