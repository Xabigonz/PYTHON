# #Resolver entre toda la clase. Un cadena en formato CSV, intentar dejarla como una simple frase.

# s="    122,Python,es,64,un,777,lenguaje,222,de,55,66,programación  "

# s = s.strip()
# a = s.split(",")
# b = [str(i) for i in a if not i.isnumeric() ]  #List comprehension.
# print(b)
# texto_final = " "

# texto_final = " ".join(str(i)for i in b) # El metodo join permite unir elementos de lista como un string.

# print(texto_final)

# print(texto_final.upper())

# print(texto_final.lower())


#Ejercicios de prueba, de list comprehension.

lista = "hola|hola|hola|hola"

a = lista.split("|")
print(a)
c = " ".join(str(i)for i in a)
print(c)