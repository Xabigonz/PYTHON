import requests

# Obtener el contenido del archivo
url = "https://raw.githubusercontent.com/itsfoss/text-files/master/agatha.txt"
response = requests.get(url)
content = response.text
print(content)

# Eliminar la línea deseada
line_to_delete = "The Mysterious Affair at Styles\n"  # La línea que deseas eliminar
content = content.replace(line_to_delete, "carmelo huele mal\n")

# Imprimir el contenido modificado
print(content)
