class vehiculo():
    def __init__(self, marca, modelo, tipoCarb, fuel_max, fuel_lvl):
        self.marca = marca
        self.modelo = modelo
        self.tipoCarb = tipoCarb
        self.fuel_max = fuel_max
        self.fuel_lvl = fuel_lvl
    def conducir(self):
        print(f"El coche está conduciendo ")
    def llenar_dep(self):
        print(f"La marca")
    def Chocar(self):
        print("El carburante del coche")
    def averiado(self):
        print("El deposito del vehiculo está lleno!")


if __name__ == "__main__":

    coches = []
    print("1. Añadir coches. \n2. Salir de la app.")
    menu=int(input("Que desea hacer? (1/2): "))
    match menu:
        case 1:
            marca = input("Inserta la marca del vehiculo: ")
            modelo = input("Inserte el modelo: ")
            tipoCarb = input("Es diesel o gasolina: ")
            fuel_lvl = int(input("Porcentaje de gasolina actual(numero solo): "))
            fuel_max = 100
            peugeot=vehiculo(marca, modelo, tipoCarb, fuel_lvl, fuel_max)
            coches.append(peugeot)
            if peugeot.fuel_lvl == peugeot.fuel_max:
                print("Esta lleno!")
            else:
                print(f"El déposito está al {fuel_lvl}%.")
                if fuel_lvl < 30:
                    print("Tienes que repostar")
                    
            if fuel_lvl != 0:
                peugeot.conducir()
            else:
                print("El coche no está conduciendo. Causa: ")

                causa = print("Estas son las posibles causas: \n 1. Está sin gasolina. \n 2. Está averiado.")
                
                match causa:
                    case 1:
            
                        pass
        case 2:
            pass




