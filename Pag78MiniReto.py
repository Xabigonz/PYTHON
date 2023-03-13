class Sistema_Nominas:
    def calcular_nominas(self, empleados):
        print('Calculando Nominas')
        print('==================')
        for empleado in empleados:
            print(f'Nomina para: {empleado.nombre}', end="")
            if isinstance(empleado, Programador):
                print(f'-{empleado.lenguaje_de_programación}', end="")
            print()
            print(f'Salario: {empleado.salario}')


class Empleado(Sistema_Nominas):
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def boostear_salario(self, salario):
        salario = salario * 1.7
        if salario == 0:
            nuevoSal = float(input("Cual es su salario actual? "))
            print(f"Salario boosteado correctamente! \n Su salario actual: {nuevoSal}€")


class Programador(Empleado):
    def __init__(self, nombre, salario, lenguaje_de_programación):
        super().__init__(nombre, salario)
        self.lenguaje_de_programación = lenguaje_de_programación 

class Analista(Empleado):
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario)

empleado1 = Empleado("Carmelo", 650)
programador1 = Programador("Carmela", 1000, "Python")


if __name__ == "__main__":
    empleados = []
    
    empleados.append(empleado1)
    empleados.append(programador1)

    sistema_nominas = Sistema_Nominas()
    sistema_nominas.calcular_nominas(empleados)

