# Pregunta 2:
# Crear un programa para:

# Imprimir los valores de esta lista, excluyendo los valores en negativo (2)
# Al imprimir, imprimes "Hola numero 6" si el valor es 6. (1)


lista = [5, 3, 12, -6, -3, 1, 6, 8, -12] # CREAR LISTA

for num in lista: 
    if num < 0:
        pass
    else:
        print(f"Numero: {num}")

#EL BUCLE RECORRE LA LISTA Y SI EL num ES < O NO HARÁ NADA Y POR EL CONTRARIO IMPRIMIRA SU VALOR.