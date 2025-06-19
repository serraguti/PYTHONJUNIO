def validarEmail(email):
    if (email.find("@") == -1):
        return False
    elif (email.count(".") == 0):
        return False
    elif (email.startswith("@") == True or email.endswith("@") == True):
        return False
    elif (email.count("@") > 1):
        return False
    elif (email.find("@") > email.rfind(".")):
        return False
    else:
        #posicion del ultimo punto
        ultimoPunto = email.rfind(".")
        #Recuperamos el dominio a partir de dicho punto en adelante
        #no queremos el punto incluido
        dominio = email[ultimoPunto + 1:]
        longitud = len(dominio)
        if (longitud >=2 and longitud <= 3):
            return True
        else:
            return False    

def getLetraNif(numeroDni):
    resultado = numeroDni % 23
    letrasDni="TRWAGMYFPDXBNJZSQVHLCKET"
    letra = letrasDni[resultado]
    return letra