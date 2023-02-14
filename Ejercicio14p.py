#PARTE 1
inflacion = 3.765
print(isinstance,float)
print(type(inflacion), id(inflacion))

# #PARTE 2

# a = 5
# b = 4.32
# c = 10

# numeros = [a, b, c]
# suma = 0

# for numero in numeros:
#     if type(numero) == int:
#         suma += numero

# print(suma)
#COMPLICACIÓNES GUAPAS



#EJERCICIO EN PIZARRA.


# Variable b con valor -1 menor que 100
b = -1
if (b < 100):
    print(f"{b} Es menor que 100")
else:
    print(f"no es menor")

# """" valor 150 mayor que 100ç
b = 150
if (b < 100):
    print(f"{b} Es menor que 100")
else:
    print(f"Es mayor que 100")
# """" valor 100 mayor igual 100.
b = 100
if (b >= 100):
    print(f"{b} Es mayor o igual a 100")
elif b > 100:
    print(f"Es mayor que 100")
else: 
    print(f"Es menor")
# """" dejar que se introduzcan valores.

num = int(input("Que numero desea usar?:"))
if (num >= 100):
    print(f"{num} Es mayor o igual a 100")
else: 
    print(f"Es menor")


