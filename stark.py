# Desafio Stark
# Industrias Stark es principalmente una empresa de defensa que desarrolla y fabrica
# armas avanzadas y tecnologías militares.

# Recientemente ha decidido ampliar su departamento de IT y para acceder a las
# entrevistas es necesario completar el siguiente desafío, el cual estará dividido en
# etapas. Cada semana recibiremos un nuevo pedido de parte de la empresa.

# La empresa compartió con todos los participantes cierta información confidencial
# de un grupo de superhéroes. Y semana a semana enviará una lista con los nuevos
# requerimientos. Quien supere todas las etapas accedera a una entrevista con el
# director para de la compañía.
# Set de datos
# La información a ser analizada se encuentra en el archivo data_stark.py, por tratarse
# de una lista, bastará con incluir dicho archivo en el proyecto de la siguiente manera:

# from data_stark import lista_personajes
# Formato de los datos recibidos


# Desafío  # 01:
# Agregar al código elaborado para cumplir el desafío  # 00 los siguientes puntos,
# utilizando un menú(genérico) que permita acceder a cada uno de los puntos por
# separado. Cada uno de los puntos debe ser desarrollado en una función distinta.
# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género M
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género F
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
# F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
# G. Recorrer la lista y determinar la altura promedio de los superhéroes de género
# M
# H. Recorrer la lista y determinar la altura promedio de los superhéroes de género
# F
# I. Informar cual es el Nombre del superhéroe asociado a cada uno de los
# indicadores anteriores(ítems C a F)
# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia(En caso de
#                                                                    no tener, Inicializarlo con ‘No Tiene’).
# M. Listar todos los superhéroes agrupados por color de ojos.
# N. Listar todos los superhéroes agrupados por color de pelo.
# O. Listar todos los superhéroes agrupados por tipo de inteligencia

from data.data import lista_personajes as lista_heroes
import os

personajes_listados = []


respuesta = 's'

while respuesta == 's':

    os.system('cls')

    while True:
        print("------- Menu de opciones ------")
        print('--------------------------------')
        print('a - LISTAR PERSONAJES MASCULINOS')
        print('b - LISTAR PERSONAJES FEMENINOS')
        print('c - OBTENER ALTURA MAX DE PERSONAJES MASCULINOS')
        print('d - OBTENER ALTURA MAX DE PERSONAJES FEMENINOS')
        print('e - OBTENER ALTURA MINIMA DE PERSONAJES MASCULINOS')
        print('f - OBTENER ALTURA MINIMA DE PERSOANJES FEMENINOS')
        print('g - OBTENER ALTURA PROMEDIO DE PERSONAJES MASCULINOS')
        print('h - OBTENER ALTURA PROMEDIO DE PERSONAJES FEMENINOS')
        print('m - OBTENER PERSONAJES ORDENADOS POR COLOR DE OJOS')
        print('j - OBTENER CANTIDAD DE OJOS DE CADA PERSONAJE')
        print('k - OBTENER CANTIDAD DE TIPOS DE PELO')
        print('l - OBTENER CANTIDAD DE TIPOS DE inteligencia')
        print('n - OBTENER PERSONAJES ORDENADOS POR COLOR DE PELO')
        print('O - OBTENER PERSONAJES ORDENADOS POR INTELIGENCIA')
        opcion = input('Ingrese lo que quiere hacer: ')
        print('\n')

        if (opcion == 'a' or opcion == 'b' or opcion == 'c' or opcion == 'd' or opcion == 'e' or opcion == 'l' or opcion == 'f' or opcion == 'j' or opcion == 'k' or opcion == 'g' or opcion == 'h' or opcion == 'm' or opcion == 'n' or opcion == 'o'):
            break

    match opcion:
        case 'a':
            listar_personajes('M')
        case 'b':
            listar_personajes('F')
        case 'c':
            get_altura_max('M')
        case 'd':
            get_altura_max('F')
        case "e":
            get_altura_min('M')
        case 'f':
            get_altura_min('F')
        case 'g':
            get_altura_promedio('M')
        case 'h':
            get_altura_promedio('F')
        case 'm':
            listar_personajes_by('color_ojos')
        case 'j':
            contar_atributos('color_ojos')
        case 'k':
            contar_atributos('color_pelo')
        case 'l':
            contar_atributos('inteligencia')
        case 'n':
            listar_personajes_by('color_pelo')
        case 'o':
            listar_personajes_by('inteligencia')

    respuesta = input('desea hacer otra cosa ? (s/n) : ')
