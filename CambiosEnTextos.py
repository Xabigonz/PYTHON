# # Pagina 33
# # ejercicio 1:

# texto = "Pitón es un lenguaje de programación. Pitón está usado para la automación, análisis de datos e incluso la creación de páginas webs. Pitón fue creado por Bill Gates en 1960. Pitón es difícil de usar."
# texto2 = texto.replace("Pitón", "Python")
# print(texto2)


# # ejercicio 2:

# texto = "    Lo más importante que nos ha mantenido en Python... bueno, hay 2 cosas importantes. Uno son las bibliotecas. La otra cosa que nos mantiene en Python, y esto es lo más importante, es facil de leer y entender. Cuando contratamos nuevos empleados. Solo digo, 'todo lo que escribas debe estar en python'. Sólo para que pueda leerlo. Y es increíble porque puedo ver desde el otro lado de la habitación, mirando su pantalla, si su código es bueno o malo. Porque un buen código de Python tiene una estructura muy obvia. Y eso hace que mi vida sea mucho más fácil        "

# t2 = texto.strip()

# contador = 0
# index = 0

# while True:
#     index = t2.find("Python", index)

#     if index == -1:
#         break
#     contador += 1
#     index += len("Python")

# print(f"La palabra Python se repite {contador} veces.")

# #Ejercicio buscar palabra + Mostrar posición (Va por caracteres)

# palabra = "código"

# if palabra in t2:
#     print("Está en el texto")
#     posi = t2.find(palabra)+ 1
#     print(f"En esta posicion: {posi}")

# else:
#     print("No está")


# # Reemplazar palabras

# remplazo = t2.replace("Python", "PYTHON")
# print(remplazo)

# # Mayus todo.

# hola= t2.upper()
# print(hola)



#GESTION CORREOS ELECTRONICOS  pag33 final.

emails = ["jon.smith@microsoft.com", "maria.fernandez@microsoft.com", "david@microsoft.com", "isabel@microsoft.es","alfonso@gmail.com"]

nombre=" "
dominios = " "

for email in emails:
    nombre,dominios=email.split("@")
    if "." in nombre:
        aux1=nombre.split(".")
        nombre_completo=" ".join(i for i in aux1)
    else:
        nombre_completo = nombre
    print(f"El nombre es: {nombre} \n El dominio es: {dominios} \n")