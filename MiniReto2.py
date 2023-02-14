#Un profesor te pide que hagas una programa que registre la asstencia de alumnos

alumnos = ["Julio", "Arturo", "Dani"]


for i in alumnos:
    asistido = input(f"{alumnos[i]} ha venido? (S/N)")
    if (asistido == "S"):
        print(f"{alumnos[i]} Ha asistido")
    else:
        print(f"{alumnos[i]} No ha asistido")