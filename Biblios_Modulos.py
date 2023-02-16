# from urllib.request import urlopen

# page = urlopen("http://info.cern.ch/")
# content = page.read() 
# print(content) 
# #Esto lo muestra como html.

# import urllib.requests

# currency = "eur"
# basecurrency = "aud"

# url = "http://freecurrencyrates.com/api/action.php?do=cvals&iso=" + currency + "&f=" + basecurrency + "&v=1&s=cbr"
# resp = requests.get(url)

# print(resp.text)
# print(resp.json())


# help("requests")

import uuid

print("El UUID uuid1() es : ", end="")
print(uuid.uuid1())

import markdown

 output = markdown.markdown("
 
 ### Se puede importar markdown a Python:
 
 
 ")