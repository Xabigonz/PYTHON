#Un profesor te pide que hagas una programa que registre la asstencia de alumnos

alumnos = ["Julio", "Arturo", "Dani"]


for alumno in alumnos:
    asistido = input(f"{alumno} ha venido? (S/N)")
    if asistido == "S":
        print(f"{alumno} Ha asistido")
    else:
        print(f"{alumno} No ha asistido")