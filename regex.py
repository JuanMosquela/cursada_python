import re

texto = "Esto es una frase para usar como modelo en la explicaion de expresiones regulares"

# retorno = re.search("a", texto)
# retorna la primer ocurrencia o None en caso de no encontrar nada
# print(retorno)
# print(retorno.group())

# # cantidad de ocurrecias
# # es keysensitive

# retorno = re.findall("o", texto)
# print(retorno)

# #podemos pedirle que nos busque literalemte una cadena

# retorno = re.findall("Modelo", texto)
# print(retorno)

# a findall podemos pasarle un tercer parametro que seria una bandera

# IGNORECASE para que no sea keysensitive
# MULTILINE para analizar multilineas

# retorno = re.findall("es", texto, re.IGNORECASE)
# print(retorno)


texto2 = """
esto es una frase
esto es una frase estoico
aaaa estoico lrase es una frase
diraccion ip crase 192:23:076
finaliza con palabra
"""

# simbolos:
# nos trae lo que inicien en e
# retorno = re.findall("^e", texto2, re.MULTILINE)
# nos trae loq ue temrine con a
# retorno = re.findall("frase$", texto2, re.MULTILINE)
# [] nos devuelve todo lo que este entre corchetes, [a-z] lo que este dentro de ese rango
# retorno = re.findall("[fra]", texto2, re.MULTILINE)

# exluir [^[0-9]] me traera todo menos lo que este despues del ^
# retorno = re.findall("[^0-9]", texto2, re.MULTILINE)


# . es un comodin
# retorno = re.findall(".rase", texto2, re.MULTILINE)
# \d me trae solos los digitos  \w solo laz letras
# \d{2} me traera todos los digitos de largo dos
# retorno = re.findall("\d{2}", texto2, re.MULTILINE)

# email = "jmosquella11@gmail.com"

# print(re.findall("@[^ ]*", email))


# # ultima palabra
# retorno = re.findall("palabra$", texto2, re.MULTILINE)
# print(retorno)

# # si uso [] significa traeme cualkquier letra que este aca dentro

# retorno = re.findall("[aeiou]", texto2, re.MULTILINE)
# print(retorno)
# print(retorno)


tema = {
    'title': 'QUEVEDO || BZRP Music Sessions #52',
    'views': 227192970,
    'length': 204,
    'img_url': 'https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg',
    'url': 'https://youtube.com/watch?v=A_g3lMcWVy0',
    'date': '2022-07-06 00:00:00'
}

# Tipo : BZRP MUSIC SESSIONS
# Artista: QUEVEDO
# Numero: 52
# Reproducciones: 227 M
# Duración: 204 segundos
# Codigo: A_g3lMcWVy0
# Fecha de carga:6/7/2022
# Hora de carga: 00:00

diccionario = {}
artista, tipo = re.split('\|\|', tema['title'])
numero = re.findall("#([^ ]*)", tema["title"])
reproducciones = re.findall("227", str(tema["views"]))
print(reproducciones)
duracion = re.findall("204", "@", str(tema["length"]))

codigo = re.search('/vi/(\w+)/', tema['img_url']).group(1)
print(codigo)

diccionario["codigo"] = re.split('\|\|', tema['img_url'])
diccionario["artista"] = artista


print(diccionario)
