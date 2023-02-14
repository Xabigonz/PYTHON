# #PAG 15 de Apuntes.

''' Preguntar al usuario por su salario. 
Multiplicar el salario que introduce el usuario por 10, 
explicándole que podría ganar tanta cantidad 
si fuera experto en Python 🤣'''

preg = int(input("Cual es su salario actual?: "))

mult = preg * 10

print(f"Si fueses un programador con mucha EXP. cobrarías {mult}")

#EJERCICIO 2

'''Preguntar al usuario por 2 números. Sumarlos y mostrar el resultado.'''

num1 = float(input("Dime un numero: "))
num2 = float(input("Dime otro numero: "))

suma = num1 + num2

print(f"la suma de estos es {suma}")

#EJERCICIO 3

'''La acción de SANTANDER va cambiando de 3.1453, 2.987 y 3.5. 
Una aplicación de mainframe con la que compartes datos 
solo quiere saber el número entero, por ejemplo, 3, 2, 3.'''

nDec = float(input("Acciones actuales de santander: "))

if nDec < 3.5:
    print(f"Las acciones actuales son de: 3")
elif nDec > 3.5:
    print(f"ERROR")
elif nDec == 3.5:
    print(f"Las acciones actuales son de: 3")


#EJERCICIO 4

'''
Crear un programa para calcular lo que cada uno tiene que pagar para la cena de una sociedad. 
Preguntar cuántas personas hay y el precio total de la compra.
Por tanto, cada uno tiene que pagar X.
'''
cPers = int(input("Cuantos estais cenando?: "))
totCen = int(input("Cuanto ha costado la cena?: "))

paInd = float(totCen / cPers)

print(f"El importe a pagar por persona es: {paInd} €")

#EJERCICIO 5

'''Crear un programa para convertir tu peso en kilos o en libras. 
Ya que sabemos usar un comando if, 
preguntar primero qué acción quiere llevar a cabo 
(“Teclear “k” si quieres convertir kilos en libras o teclear “l” 
si quieres convertir libras en kilos”).'''

metodo = input("Kilos o Libras(Inserte K para kilos y L para libras): ")
if metodo == "K":
    peso1 = float(input("Inserte el peso a intercambiar: "))
    cambio1 = float(peso1 * 2.205)
    print(f"Este es el equivalente a lo que pidió: {cambio1}")
elif metodo == "L":
    peso2 = float(input("Inserte el peso a intercambiar: "))
    cambio2 = float(peso2 / 2.205)
    print(f"Este es el equivalente a lo que pidió: {cambio2}")


#EJERCICIO 6

'''Has visto este código en una página web. 
Adivinar el tipo de dato que hay un la variable a.
En otra página, ejecutan la función de esta forma.
a, b, c = numbers()
¿Qué tipo de datos son a, b y c?
'''
a = "algo"
b = 3
c = True

print(type(a), type(b), type(c))

#OPCIONAL
numAl = 2.4596

print(f'Formateado con %3f y %2f %3f{numAl:.1f}' )
# Redondea el resultado automaticamente
