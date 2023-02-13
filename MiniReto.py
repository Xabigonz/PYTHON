#CALCULADORA DE IVA


precioBase = float(input("Inserte el precio sin IVA: "))
porcIVA = float(input("Inserte el porcentaje de IVA(Solo el numero): "))

precioConIVA = (precioBase * (porcIVA/100 + 1))
cantidadIVA = (precioConIVA - precioBase)
# precioFinal = 
print(f"El precio final con la aplicacion del IVA es de: {precioConIVA} ")
print(f"La cantidad de IVA aplicada es: {cantidadIVA}")

