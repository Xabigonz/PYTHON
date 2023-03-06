class Perro():
    def __init__(self, nombre, raza, altura, edad):
        self.nombre = nombre
        self.raza = raza
        self.altura = altura
        self.edad = edad
        
    def comer(self):
        print("Esta comiendo")
    def dormir(self):
        print("Está dormido, no le toques los huevos rey")
    def ladrar(self):
        print("Guau")
    def __str__(self):
        print(f"Los datos de su perro: \n Nombre: {nombre} \n Raza: {raza} \n Estatura: {altura} \n Edad: {edad}")


#Para realizar ejercicios siempre utilizar un main:



#Match case:

if __name__=="__main__":
    perros = []

    print("1. Añadir perros. \n2. Salir de la app.")
    
    accion=int(input("Que desea hacer (1/2): "))
    match accion:
        case 1:
            
            nombre = input("Inserte el nombre de su perro: ")
            raza = input("Digame su raza: ")
            altura = input("Proceda a mostar su estatura: ")
            edad = input("Introduce su edad: ")
    
            perriko = Perro(nombre, raza, edad, altura)
            perros.append(perriko)
            
            perriko.__str__(1)
        case 2:
            pass