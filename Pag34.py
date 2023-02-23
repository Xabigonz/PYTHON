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

print(os.environ)
print(os.getlogin)

