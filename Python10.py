def imprimirMens(lenguaje):
    print(f"carmelo {lenguaje}")
    

def calculo(a):
    return a+a+a+a

#Lo que añades dentro de las parentesis es para darle un valor a la variable.

if __name__ == '__main__':
    x = imprimirMens("Python")
    y = calculo(5)
    print(x, y)


def sumar(x,y):
    return x + y        #Obligatorio poner el return antes de lo que queramos que haga, si no no devuelve nada.

if  __name__ == '__main__':
    x = sumar(6,4)
    print(x)
