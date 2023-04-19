
# CLASE PADRE

class Animal():
    def __init__(self, nombre, raza, patas, tipo): # ATRIBUTOS, definir atributos
        self.nombre = nombre
        self.raza = raza
        self.patas = (2,4)
        self.tipo = tipo

    # METODOS
    def hacerRuido(self):
        if self.tipo == "Perro":    # CONDICIONAR TIPOS
            print("Woof, Woof!")
        else:
            print("Tweet, Tweet!")

    def correr(self):
        if self.tipo == "Perro":
            print("Estoy corriendo!")

    def volar(self):
        if self.tipo == "Pajaro":
            print("Estoy volando!")

# CLASE HIJA
class Perro(Animal):
    def __init__(self, nombre, raza, patas, tipo): # ATRIBUTOS
        super().__init__(nombre, raza, patas, tipo) # Lo que hereda de la clase padre


# CLASE HIJA
class Pajaro(Animal):
    def __init__(self, nombre, raza, patas, tipo):
        super().__init__(nombre, raza, patas, tipo)




# Crear código para instanciar un Perro (1)

bulldog = Perro("Txusti", "buldog", 4, "Perro") # DAMOS LOS PARAMETROS NECESARIOS
# LLAMADA A LOS METODOS
bulldog.hacerRuido()
bulldog.correr()

