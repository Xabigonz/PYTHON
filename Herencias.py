class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"Mi nombre es: {nombre} \n Edad: {edad}")
    def hablar(self):
        print(f"Hola guenas tardes, zoy {self.nombre} ")


jon = Persona("Jon", 18)
carmel=Persona("Carmel", 24)

carmel.hablar()
jon.hablar()


if __name__ == "__main__":
    nombre= input("Introduce el nombre de la nueva persona: ")
    edad = int(input("Introduce su edad: "))
    nombre = Persona(nombre,edad)
