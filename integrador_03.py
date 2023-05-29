from functions.stark_functions import *
from functions.funciones import *


options = ["a - LISTAR PERSONAJES MASCULINOS",
           "b - LISTAR PERSONAJES FEMENINOS",
           "c - OBTENER ALTURA MAX DE PERSONAJES MASCULINOS",
           "d - OBTENER ALTURA MAX DE PERSONAJES FEMENINOS",
           "e - OBTENER ALTURA MINIMA DE PERSONAJES MASCULINOS",
           "f - OBTENER ALTURA MINIMA DE PERSOANJES FEMENINOS",
           "g - OBTENER ALTURA PROMEDIO DE PERSONAJES MASCULINOS",
           "h - OBTENER ALTURA PROMEDIO DE PERSONAJES FEMENINOS",
           "m - OBTENER PERSONAJES ORDENADOS POR COLOR DE OJOS",
           "j - OBTENER CANTIDAD DE OJOS DE CADA PERSONAJE",
           "k - OBTENER CANTIDAD DE TIPOS DE PELO",
           "l - OBTENER CANTIDAD DE TIPOS DE inteligencia",
           "n - OBTENER PERSONAJES ORDENADOS POR COLOR DE PELO",
           "O - OBTENER PERSONAJES ORDENADOS POR INTELIGENCIA",
           "Z - SALIR"]


# generar_menu(options)


# data = abrir_json("data.json")
data = abrir_csv("data.csv")


print(data)
