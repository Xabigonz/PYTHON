import getpass
#Ejercicio 1

contra = str("123456")
intentos = 5


for i in range(intentos):
    pregunta = getpass.getpass("Introduzca la contraseña: ")
    
    if pregunta != contra:
        intentos -=1
        print("La contraseña es incorrecta")
        print(f"Le quedan {intentos}.")

    elif pregunta==contra:
        print("Es correcta \n Bienvenido de nuevo REY!" )
        break
        
#Mejoras

nContra = getpass.getpass("Inserte su nueva contraseña: ")

i = 0


while i < len(nContra):
    i += 1
    a=nContra.replace(nContra,"*")
    
    

