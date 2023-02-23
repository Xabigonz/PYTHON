import requests

link = "http://info.cern.ch/"
r = requests.get(link)
print(r.status_code)  # Código de http.

html = r.text
lineas_html = html.splitlines()

for linea in lineas_html:
    linea_encriptada = ""
    for caracter in linea:
        codigo_ascii = ord(caracter) + 1
        linea_encriptada += str(codigo_ascii)
    print(linea_encriptada)

import os

print(os.environ) # Este diccionario proporciona acceso a las variables de entorno a través de claves.
print(os.getlogin) #Ver quien y que está usando el usuario actual.
print(os.getcwd)  
print(os.listdir())  #Imprime el contenido del directorio actual.



def eliminadorCarpetas():

    borral = os.rmdir("C:/Users/xabig/OneDrive/Escritorio/BORRA_CARPETA")

    path = "C:/Users/xabig/OneDrive/Escritorio/BORRA_CARPETA"
    borrado = os.rmdir(path)
    print(borrado) # Esto imprimirá "None" si se eliminó la carpeta correctamente
