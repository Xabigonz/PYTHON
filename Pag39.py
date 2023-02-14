#Número Aleatorio del 1 al 100.
import random

numeroAdiv = random.randint(0, 100)

while True:
    pregunta = int(input("Intenta adivinar el número aleatorio del 1 al 100: "))
    if pregunta < numeroAdiv:

        print(f"El numero es mayor, ")

    elif pregunta > numeroAdiv:

        print(f"El numero es menor, ")

    else:

        print (f"El numero es correcto, es {numeroAdiv}")
        break
