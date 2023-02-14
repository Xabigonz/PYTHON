#Número Aleatorio del 1 al 100.
import random

numeroAdiv = random.randint(0, 100)

pregunta = int(input("Intenta adivinar el número aleatorio del 1 al 100: "))
try2 = int(input("El numero es menor, inténtalo de nuevo: "))
try3 = int(input("El numero es mayor, inténtalo de nuevo: "))

while pregunta != numeroAdiv:
    print(pregunta)
    if pregunta > numeroAdiv:
        
        
        print(try2)
    elif try2 < numeroAdiv:
        print(try3)
    else:
        print(f"Es correcto el numero es {numeroAdiv}")
