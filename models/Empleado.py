from models.persona import Persona

class Empleado(Persona):
    #AHORA MISMO UN EMPLEADO TIENE LO MISMO QUE UNA PERSONA
    #PODEMOS IMPLEMENTAR CARACTERISTICAS QUE NO TIENE UNA PERSONA
    def __init__(self):
        #podemos llamar (buena praxis)
        #al constructor de la clase de la que heredamos
        super().__init__()
        self.nombre = "Empleado"
        self.apellidos = "Del mes"
        self.salario = 1700
        # self.pais = "Spain"

    def __str__(self):
        return self.nombre + " " + self.apellidos

    #TAMBIEN PODEMOS CREAR METODOS SI LO DESEAMOS
    def getVacaciones(self):
        return 50