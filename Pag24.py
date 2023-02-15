#Programa de gestión de fiestas


MAX_INVITADOS = 5

gente = int(input("Cuantos sois?: "))
invitados = []

if gente > MAX_INVITADOS:
    print(f"Lo siento rey ta petao, solo se pueden {MAX_INVITADOS}")
    
elif gente <= MAX_INVITADOS:
    
    for i in range(gente):
        
        invitado = input("Como te llamas?: ")
        print("Apuntado brodel, disfruta")
        invitados.append(invitado)
print(f"Estos son los invitados: \n{invitados}")        
 
        