class Persona:
    #TENEMOS DOS FORMAS DE DECLARAR PROPIEDADES
    #1) AQUI AL INICIO DE LA CLASE
    # nombre = ""
    # apellidos = ""
    # edad = 0
    # pais = "lo que sea"

    #EL CONSTRUCTOR ES UN METODO PARA CREAR PROPIEDADES
    #E INICIAR DICHAS PROPIEDADES
    #2) CREAR LAS PROPIEDADES EN EL CONSTRUCTOR
    def __init__(self):
        #PODEMOS TENER PROPIEDADES PRIVADAS
        #UNA PROPIEDAD PRIVADA SE CREA MEDIANTE EL DOBLE GUION BAJO
        # private:  __propiedadPrivada
        self.__dni = "12345678X"
        self.pais = "Alemania"
        self.edad = 0
        self.nombre = ""
        self.apellidos = ""
    #CREAMOS UN METODO PARA VER QUE PODEMOS ACCEDER AL DNI
    def getPrivateDni(self):
        return self.__dni
    
    #CREAMOS UN METODO QUE NOS DEVUELVA EL NOMBRE Y APELLIDOS DE UNA PERSONA
    def getNombreCompleto(self, dato: int):
        return self.nombre + " " + self.apellidos
    
    # #ME GUSTARIA TENER UN METODO QUE NOS DEVOLVIERA LOS APELLIDOS Y NOMBRE
    # def getNombreCompleto(self, **kwargs):
    #     return self.apellidos + " " + self.nombre
    
    # #ME GUSTARIA TENER UN METODO QUE NOS DEVOLVIERA LOS APELLIDOS Y NOMBRE
    # def getNombreCompleto(self, mayusculas, param2):
    #     return self.nombre.upper() + " " + self.apellidos.upper()    