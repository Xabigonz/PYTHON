import numpy as np
#Un profesor te pide que hagas una programa que registre la asstencia de alumnos

#No es la mejor forma de hacerlo con la lista, 
# sino con el diccionario que es una especie de tabla.

alumnos = ["Julio", "Arturo", "Dani"]
asistiencia = []
total = 0

for alumno in alumnos:
    asistido = input(f"{alumno} ha venido? (S/N)")
    if asistido == "S":
        print(f"{alumno} Ha asistido")
        asistiencia.append({alumno,  "\u2713"})
        total = total + 1
        
    else:
        print(f"{alumno} No ha asistido")
        asistiencia.append({alumno, "x"})
print(asistiencia)
print(f"Han asisitido {total} alumnos.")

#Ahora hay que hacer que muestre 
#la media que han sacado los alumnos en el examén

notas = [4,8,9]
avg = np.mean(notas)
print(f"Estás son las notas que habeis obtenido: {notas} \n"
       f"y estas la media de clase {avg}")