<<<<<<< HEAD
print("hola")
help("keywords")
help("for")

import keyword
a = keyword.kwlist
print(type(a))

num = 13.2340
print(num)

print(type(num))
print(isinstance, num)

x = 10
#print(hex(id(x)))
print(id(x))

x = 20
print(id(x))

#Mas ejemplos

nombres = ["Jon", "Jon", "Jon"]

print(id(nombres))

nombres.append("pedro")

print(id(nombres))


# Ejemplo rayante:

str1 = "PYTHON"
str2 = str1
print(id(str2))
del str1
print(id(str2))

exists = False
if exists == True:
    print("TRUE")
    print("True")
print("END") #Su posicion más retrasada significa que esta fuera del if().

x = 3 
if(x >= 1):
    print("mas que uno")
elif (x < 3) and (y < 3):
    print("algo mi loko")
else:
    print("end")

list = [262, 444, "Maria"]

for i in list:
    print(i)


x = range(10)
=======
print("hola")
help("keywords")
help("for")

import keyword
a = keyword.kwlist
print(type(a))

num = 13.2340
print(num)

print(type(num))
print(isinstance, num)

x = 10
#print(hex(id(x)))
print(id(x))

x = 20
print(id(x))

#Mas ejemplos

nombres = ["Jon", "Jon", "Jon"]

print(id(nombres))

nombres.append("pedro")

print(id(nombres))


# Ejemplo rayante:

str1 = "PYTHON"
str2 = str1
print(id(str2))
del str1
print(id(str2))

exists = False
if exists == True:
    print("TRUE")
    print("True")
print("END") #Su posicion más retrasada significa que esta fuera del if().

x = 3 
if(x >= 1):
    print("mas que uno")
elif (x < 3) and (y < 3):
    print("algo mi loko")
else:
    print("end")

list = [262, 444, "Maria"]

for i in list:
    print(i)


x = range(10)
>>>>>>> 6bfe401c2c60da2acc4d4ccdaeba2f48aa1da638
print(x)