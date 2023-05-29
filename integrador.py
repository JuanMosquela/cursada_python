from data.data import lista_personajes
from functions.stark_functions import *
from functions.funciones import *


lista = normalize_data(lista_personajes)


# nombre = obtener_nombre(lista_personajes[0])


# imprimir_nombres_heros(lista_personajes)
# obtener_nombre_dato(lista_personajes[0], "fuerza")
# imprimir_nombres_alturas(lista_personajes)
# hero_name, valor_max = calcular_value(lista, "peso")
# print(hero_name, valor_max)
# total = sumar_dato_hero([], "peso")
# print(f"La suma de todos los heroes de es {total}")
# resultado = dividir(4, 2)
# print(resultado)
# promedio = calcular_promedio(lista, "altura")
# print(promedio)

nuevo = sort(lista, "fuerza", False)
print(nuevo)
