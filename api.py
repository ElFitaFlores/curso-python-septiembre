# API REST
# URL - https://google.com/fotos
# Métodos - GET POST PUT DELETE
# Body - {"name": "Rafael Flores", "bithdate": "1992-11-27"}
# Encabezados AUTHENTICATION: Bearer xxx-123456, Content-Type: application/jpg Accept: text
# Path parameters https://www.google.com/fotos/1
# Query params https://google.com/fotos?q=python

import requests

response = requests.get('https://www.breakingbadapi.com/api/character/random')
#print(response.json())
personaje = response.json()[0]
print(personaje['name'])
#print(personaje['birthday'])