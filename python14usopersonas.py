from models.persona import Persona
from models.Empleado import Empleado
from models.Director import Director
persona1 = Persona()
persona2 = Persona()
persona3 = Persona()
listaPersonas = []
listaPersonas.append(persona1)
listaPersonas.append(persona2)
listaPersonas.append(persona3)
print("Probando la clase Persona de POO")
empleado = Empleado()
#DIBUJAMOS UN EMPLEADO
print(empleado)
# print(f"Vacaciones empleado: {empleado.getVacaciones()}")
dire = Director()
# print(f"Vacaciones director: {dire.getVacaciones()}")
# print(f"Salario: {empleado.salario}")
# #UNA PERSONA EL CREARSE ES ALEMANA, UN EMPLEADO SERA IGUAL?
# print(f"Nacionalidad: {empleado.pais}, Edad: {empleado.edad}")
# empleado.nombre = "Empleado"
# empleado.apellidos = "Empleado"
# print(f"empleado Nombre: {empleado.nombre}, Apellidos: {empleado.apellidos}")

# #CREAMOS UNA INSTANCIA DE PERSONA
# personaje = Persona()
# personaje.nombre = "Sheldon"
# personaje.apellidos = "Cooper"
# print(personaje.getNombreCompleto()) #normal
# # print(personaje.getNombreCompleto(22)) #reves
# # print(personaje.getNombreCompleto(33,33))
# print(f"Nacionalidad: {personaje.pais}, Edad: {personaje.edad}")
# #ENCAPSULACION
# print(personaje.getPrivateDni())
