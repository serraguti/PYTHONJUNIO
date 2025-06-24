from models.Empleado import Empleado
class Director(Empleado):
    #necesitamos que un director tenga mas dias que un empleado
    #cambiamos el metodo
    def getVacaciones(self):
        #CON LA PALABRA super() PODEMOS INVOCAR A 
        #LOS METODOS DE LA CLASE QUE HEREDAMOS (Empleado)
        vacaciones = super().getVacaciones()
        return vacaciones + 8
    def mandar(self):
        print("Soy el jefe de todo!!!")