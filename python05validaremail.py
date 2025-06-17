print("Validacion email string")
email = input("Introduzca email: ")
# •	Que el email contenga @
# •	Que el email contenga .
# •	@ ni al inicio ni al final
# •	Solamente una @ en el email
# •	Que exista un punto después de la @
# •	Dominio de 2 a 3 caracteres
if (email.find("@") == -1):
    print("No existe @")
elif (email.count(".") == 0):
    print("Email sin punto")
elif (email.startswith("@") == True or email.endswith("@") == True):
    print("@ al inicio o al final")
elif (email.count("@") > 1):
    print("Tenemos más de una @")
elif (email.find("@") > email.rfind(".")):
    print("Debe existir un punto después de @")
else:
    #posicion del ultimo punto
    ultimoPunto = email.rfind(".")
    #Recuperamos el dominio a partir de dicho punto en adelante
    #no queremos el punto incluido
    dominio = email[ultimoPunto + 1:]
    longitud = len(dominio)
    if (longitud >=2 and longitud <= 3):
        print(f"Email correcto: {email}")
    else:
        print("Dominio de dos a tres caracteres")
print("Fin de programa")