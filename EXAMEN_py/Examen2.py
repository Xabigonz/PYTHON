# Pregunta 2:
# Crear un programa para:

# Imprimir los valores de esta lista, excluyendo los valores en negativo (2)
# Al imprimir, imprimes "Hola numero 6" si el valor es 6. (1)


lista = [5, 3, 12, -6, -3, 1, 6, 8, -12] # CREAR LISTA

for num in lista: 
    if num < 0:
        pass
    else:
        print(f"Hola numero: {num}")

#EL BUCLE RECORRE LA LISTA Y SI EL num ES < O NO HARÁ NADA Y POR EL CONTRARIO IMPRIMIRA SU VALOR.



# Pregunta 3:
# Teniendo un rectángulo de 10 metros de base y 3 metros de altura, crear una función para calcular su área.

# Acciones:

# Crear la función (2)
# Ejecutar la función con valores que proporciona el usuario (1)
# Modificar la función para que si el usuario ejecuta area(10), por defecto coge el valor 3 de altura (1)



# INFORMACION DEL TRIANGULO
baseRec = 10
altRec = 3



pregUser = int(input("Desea insertar valores o calcular el area del triangulo? (1/2)"))
while True:
    if pregUser == 1:
        baseRec = int(input("Inserta el balor de la base: "))
        altRec = int(input("Inserta el balor de la altura: "))
        area = (baseRec * altRec)/2
    elif pregUser == 2:
        area = (baseRec*altRec)/2        
        print(f"El area del triangulo es {area}")

        
