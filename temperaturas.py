# Consideraciones:
# 1. Utilizar listas, diccionarios, tuplas de manera óptima para el manejo de los
# datos solicitados.
# 2. Aplicar funciones de manera que el programa quede modularizado y que las
# funciones sean lo más genéricas posibles para lograr reutilizarlas.
# 3. Parametrizar funciones de manera adecuada y utilizar los retornos para evitar
# (en lo posible) funciones que no retornan nada y no reciban nada.
# 4. Evitar el uso de funciones predefinidas del lenguaje, como max, in, count. En
# lo posible pensar en un algoritmo que dé solución al problema.
# 5. Aplicar reglas de estilo vistas en la cátedra.

# Realizar un programa que permita el ingreso de temperaturas a lo largo de una
# semana (Los 7 días de la semana, no necesariamente se ingresan en orden. Por
# ejemplo, puedo cargar primero el miércoles, luego el domingo, etc.). Dadas estas
# temperaturas debemos obtener distintas estadísticas.
# Para ello se deberán implementar distintas funciones:
# 1. Una que permita la carga de todas las temperaturas (día y temperatura).
# 2. Una que permita el pedido y validación de una temperatura. La misma
# retornará una temperatura válida.
# 3. Una que reciba como parámetro la lista y retorne el promedio de
# temperaturas.
# 4. Una que calcule la temperatura máxima.
# 5. Una que gestione un menú de usuario, el cual deberá tener las siguientes
# opciones:
# a. Cargar temperaturas
# b. Mostrar temperaturas (junto con sus días)
# c. Mostrar máxima temperatura con su día. (tener en cuenta que puede
# haber varios días con la misma temperatura)
# d. Mostrar promedio.
# e. Salir

# Nota: No se podrá entrar a las opciones b, c y d si no se cargaron los datos en la
# opción a.

import os

from functions.funciones import *

lista_semanal = []


def calcular_temp_max(lista):

    bandera = True

    for dia in lista:
        if (bandera or dia['temperatura'] > temp_max):
            bandera = False
            dia_temp_max = dia['dia']
            temp_max = dia['temperatura']

    return (temp_max, dia_temp_max)


def promedio_dias(lista):
    acumulador_temp = 0
    for dia in lista:
        acumulador_temp += dia['temperatura']

    promedio = acumulador_temp / len(lista_semanal)

    return promedio


def pedir_temperatura():
    while True:
        temperatura = pedir_num('Ingrese la temperatura del dia : ')

        if (temperatura < -40 or temperatura >= 50):
            print('La temperatura no puede ser menor a -40° o mayor a 50°')

        else:
            return temperatura


def cargar_dias():
    for i in range(4):

        dia_diccionario = {}

        dia = pedir_texto('Ingrese el dia de la semana : ')

        if i == 0:

            # si es la primera iteracion insertamos los datos

            dia_diccionario['dia'] = dia
            temperatura = pedir_temperatura()
            dia_diccionario['temperatura'] = temperatura
            lista_semanal.append(dia_diccionario)
        else:

            # de lo contrario checkeamos si ese el dia que queremos ingresar no esta previamente insertado

            for elemento in lista_semanal:
                while dia == elemento['dia']:
                    dia = pedir_texto(
                        'Dia ingresado ya existe, vuelva a ingresar otro diferente : ')

            dia_diccionario['dia'] = dia
            temperatura = pedir_temperatura()
            dia_diccionario['temperatura'] = temperatura
            lista_semanal.append(dia_diccionario)


def mostrar_lista(lista):
    if len(lista) > 0:
        for dia in lista:
            print(dia)
    else:
        print('Todavia no cargaste valores en la lista')


respuesta = 's'
lista_cargada = False

while respuesta.lower() == 's':

    os.system('cls')

    while True:
        print("------- Menu de opciones ------")
        print('--------------------------------')
        print('a - Cargar Datos en la Lista ')
        print('b - Cargar Datos en la Lista ')
        print('c - Cargar Datos en la Lista ')
        print('d - Cargar Datos en la Lista ')
        print('e - Salir')
        opcion = input('Ingrese lo que quiere hacer: ')
        print('\n')

        if (opcion == 'a' or opcion == 'b' or opcion == 'c' or opcion == 'd' or opcion == 'e'):
            break

    match opcion:
        case 'a':

            cargar_dias()
            lista_cargada = True
        case 'b':

            mostrar_lista(lista_semanal)

        case 'c':
            if lista_cargada:
                temp_max, dia_max = calcular_temp_max(lista_semanal)
                print(
                    f'La temperatura maxima semanal fue de {temp_max} en el dia {dia_max}')
            else:
                print('Para usar esta funcion primero debes cargar la lista')

        case 'd':
            if lista_cargada:
                promedio_dias(lista_semanal)
                print(
                    f"el promedio de las temperaturas es de {promedio_dias(lista_semanal)}")
            else:
                print('Para usar esta funcion primero debes cargar la lista')

        case 'e':
            break

    respuesta = input('quiere hacer otra cosa ? (s/n) : ')
