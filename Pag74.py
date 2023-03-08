class vehiculo():
    def __init__(self, marca, modelo, tipo, tipoCarb, fuel_lvl, ruedas, color):
        self.marca = marca
        self.modelo = modelo
        self.tipoVei = tipo
        self.tipoCarb = ("Gasolina", "Diesel")
        self.fuel_max = 100
        self.fuel_lvl = fuel_lvl
        self.ruedas = (2,3,4)
        self.color = color

    def conducir(self):
        print(f"El coche está conduciendo ")
    def Chocar(self):
        print("Has chocado rey...")
    def averiado(self):
        print("El deposito del vehiculo está lleno!")
    def llenarDeposito(self):
        if self.fuel_lvl != self.fuel_max:
            diferencia = self.fuel_max - self.fuel_lvl
            self.fuel_lvl = self.fuel_max
            print("Llenado satisfactoriamente (mientras tanto tu riñon...)")
            print(f"Ha llenado {diferencia} % restante.")
        else:
            print("El deposito está a tope rey, cuando se gaste vuelva rellenarlo.")
            


#CLASES HIJO que van a heredar de la anterior:
class Camion(vehiculo):
    def __init__(self,  marca, modelo, tipo, tipoCarb, fuel_lvl, ruedas, color):
        super().__init__(marca, modelo, tipo,tipoCarb, fuel_lvl, ruedas, color)
        
    def Dormir():
        pass
    def Transportar_Productos():
        pass
class Moto(vehiculo):
    def __init__(self, marca, modelo, tipo, tipoCarb, fuel_lvl, ruedas, color):
        super().__init__(marca, modelo, tipo, tipoCarb, fuel_lvl, ruedas, color)
        
    def HacerCaballito():
        print("Está haciendo el caballito")


#CREACION DE MOTO
moto= Moto("Yamaha","S 700", "Moto", "Gasolina", 17, 2, "Rojo")
moto.llenarDeposito()

#CREACION DE CAMION
camion = Camion("MAN", "R 750", "Camion", "Diesel", 100, 4, "Blanco" )
camion.llenarDeposito()