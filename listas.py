# 2----------------------------------------------

# La real academia española nos pide desarrollar un pequeño programa que contenta el
# diccionario de la lengua española y su traducción al inglés. Para esto necesitamos un
# algoritmo que nos permita el ingreso de una palabra en español y su traducción al
# ingles y guardarlo en una lista. Si la palabra no existe, debemos agregarla, y si la
# palabra existe debemos informar que la palabra ya existe y su índice dentro del listado,
# esta carga debe ser hasta que el usuario se canse de ingresar palabras. Al finalizar se
# debe mostrar todo el listado de palabras ingresadas con su palabra equivalente en
# inglés. Recordar validar los datos de forma correcta.

from functions.funciones import *

palabra = None
respuesta = 's'
bandera = True
lista_palabras = []
while respuesta == "s":

    diccionario = {}

    if bandera:
        bandera = False
        palabra = pedir_texto('Ingrese una palabra en español: ')
        diccionario['palabra'] = palabra
        traduccion = pedir_texto('Ingrese la traduccion de la palabra: ')
        diccionario['traduccion'] = traduccion
    else:
        palabra = pedir_texto('Ingrese una palabra en español: ')
        for elemento in lista_palabras:
            if palabra == elemento['palabra']:

                while palabra == elemento['palabra']:
                    palabra = pedir_texto(
                        f'La palabra ya se encuentra en la lista en la posicion {lista_palabras.index(elemento)}, ingresa otra :')
            else:
                diccionario['palabra'] = palabra
                traduccion = pedir_texto(
                    'Ingrese la traduccion de la palabra: ')
                diccionario['traduccion'] = traduccion

    lista_palabras.append(diccionario)

    respuesta = input('Desea ingresar otra palabra? (s / n): ')

for item in lista_palabras:
    print(item)

# 4----------------------------------------------

# Debemos desarrollar un algoritmo que permita computar los votos del Senado de
# Berlinberlín. Se deberá ingresar el nombre de cada senador y si está Presente o no en
# la sesión. Si el senador está presente, se deberá pedir el valor del voto
# El voto de los senadores berliberlineses puede ser Afirmativo, Negativo o Abstención
# (validar). El valor por defecto para los senadores ausentes será Abstención.
# Se deberá Informar:

# o Cantidad total de senadores.
# o Cantidad de senadores presentes.
# o Cantidad y porcentaje de votos afirmativos.
# o Cantidad y porcentaje de votos negativos.
# o Cantidad y porcentaje de abstenciones.
# o Generar una lista de senadores por cada tipo de voto y mostrarlas por
# pantalla.

# respuesta = 's'
# lista_senadores = []
# lista_estado = []
# lista_votos = []

# contador_presentes = 0
# contador_afirmativos = 0
# contador_negativos = 0
# contador_abstenciones = 0

# while respuesta == 's':
#     while True:
#         senador = input('ingrese el nombre del senador: ')
#         if senador != '':
#             break

#     while True:
#         estado = input('ingrese el estado del senador: (presente - ausente) ')
#         if estado == 'presente' or estado == 'ausente':
#             break

#     if (estado == 'presente'):
#         while True:
#             voto = input(
#                 'ingrese su voto (afirmativo - negativo - abstencion)')
#             if (voto == 'afirmativo' or voto == 'negativo' or voto == 'abstencion'):
#                 break
#     else:
#         voto = 'abstencion'

#     match(voto):
#         case 'afirmativo':
#             contador_afirmativos += 1
#         case 'negativo':
#             contador_negativos += 1
#         case 'abstencion':
#             contador_abstenciones += 1

#     lista_senadores.append(senador)
#     lista_estado.append(estado)
#     lista_votos.append(voto)

#     respuesta = input('Desea ingresar otro senador? (s / n) :')

# for estado in lista_estado:
#     if (estado == 'presente'):
#         contador_presentes += 1


# print(f'La cantidad total de senadores es de {len(lista_senadores)} senadores')
# print(f'La cantidad total de votos positivos es de {contador_afirmativos} ')
# print(f'La cantidad total de votos negativos es de {contador_negativos} ')
# print(f'La cantidad total de abstenciones es de {contador_abstenciones} ')

# 5--------------------------------------------------

# Para una veterinaria se pide clasificar el ingreso de pacientes hasta que el usuario
# quiera (se limita a 1 perrito por ingreso), se les pide:
# nombre, precio de la consulta (validar entre 500$ y 2500$) raza: (validar entre caniche,
# ovejero, siberiano), edad (validar 1 a 15) y peso (entre 25 y 40 kilos) determinar:

# 1. Generar un listado con todos los datos de los pacientes ordenados por edad.
# 2. Generar un listado de los perros que pesen más de 30 kilos y ordenarla por
# nombre.
# 3. Si la facturación en bruto supera los 5000$, hay que agregarle un 21% de
# impuesto por ingresos brutos e informarlo.
# 4. Informar el nombre y el peso del perro con más peso.

# respuesta = 's'
# lista_pacientes = []
# perros_mayor_edad = []
# bandera = True
# max_peso = None
# perro_mas_pesado = None
# acumulador_facturacion = 0

# while respuesta == 's':

#     perrito = {}

#     while True:
#         nombre = input('Ingrese el nombre del paciente: ')
#         if (nombre != '' and nombre.isalpha()):
#             break

#     perrito['nombre'] = nombre

#     while True:
#         try:
#             precio = int(
#                 input('Ingrese el precio  de la consulta (entra $500 y $2500): '))
#             if (precio >= 500 and precio <= 2500):
#                 break
#         except:
#             print('el valor ingresado no es valido')

#     perrito['precio'] = precio
#     acumulador_facturacion += precio

#     while True:
#         raza = input(
#             'Ingrese la raza  del perrito (caniche - ovejero - siberiano): ')
#         if (raza == 'caniche' or raza == 'ovejero' or raza == 'siberiano'):
#             break

#     perrito['raza'] = raza

#     while True:
#         try:
#             edad = int(input('Ingrese la edad  del perrito (entra 1 y 15): '))
#             if (edad >= 1 and edad <= 15):
#                 break
#         except:
#             print('el valor ingresado no es valido')

#     perrito['edad'] = edad

#     while True:
#         try:
#             peso = int(
#                 input('Ingrese la edad  del perrito (entra 25kg y 40kg): '))
#             if (peso >= 25 and peso <= 45):
#                 break
#         except:
#             print('el valor ingresado no es valido')

#     perrito['peso'] = peso

#     lista_pacientes.append(perrito)

#     respuesta = input('Desea ingresar otro perrito (s/n): ')


# print(lista_pacientes)

# lista_pacientes.sort(key=lambda x: x.get('edad'))
# print(f'Pacientes ordenados por edad: {  lista_pacientes}')


# for perro in lista_pacientes:
#     if (perro['peso'] > 30):

#         perros_mayor_edad.append(perro)

# if (len(perros_mayor_edad) > 0):
#     print(
#         f"Lista de perros que pesean mas de 30kg ordenaos por nombre: {perros_mayor_edad.sort(key=lambda x: x.get('nombre'))}")

# for perro in lista_pacientes:
#     if (bandera or perro['peso'] > max_peso):
#         bandera = False
#         max_peso = perro['peso']
#         perro_mas_pesado = perro['nombre']

# print(
#     f'El nombre y peso del perro mas pesado es : {perro_mas_pesado} y su peso es de {max_peso} ')


# def obtenerDescuento(precio):
#     IVA = 21
#     aumento = (precio) * IVA / 100
#     precio_final_descuento = acumulador_facturacion + aumento
#     return precio_final_descuento


# if (acumulador_facturacion > 5000):
#     print('facturacion de mas de 5000')
#     print(
#         f"El precio final, habiendole aplicado un aumento del 21%, es de : {obtenerDescuento(acumulador_facturacion)}")


# 6------------------------------------------------

# Se nos pide realizar un programa que le pida al usuario una N cantidad de veces y
# calcular la máxima diferencia en la secuencia de números ingresada.

# respuesta = 's'
# lista_numeros = []
# bandera = True
# valor_minimo = None
# valor_maximo = None

# while respuesta == 's':
#     while True:
#         try:
#             numero = int(input('Ingrese un numero para agregar a la lista : '))
#             if (numero != ''):
#                 break
#         except:
#             print('no es un valor valido')

#     lista_numeros.append(numero)

#     if (bandera):
#         bandera = False
#         valor_minimo = numero
#         valor_maximo = numero
#     else:
#         if (numero > valor_maximo):
#             valor_maximo = numero
#         else:
#             valor_minimo = numero

#     respuesta = input('Desea ingresar otro numero (s/n): ')

# print(lista_numeros)


# if (len(lista_numeros) >= 2):
#     diferencia = valor_maximo - valor_minimo
#     print(diferencia)

# 7-------------------------------------------

# Un grupo de cinco amigos se juntan para jugar una partida de CS:GO, deciden que
# van a jugar 10 partidas y necesitan realizar datos estadísticos sobre las partidas
# jugadas. Para eso necesitan ingresar los siguientes datos en el siguiente orden
# especifico: nombre, edad, bajas confirmadas (el murió), muertes confirmadas (el mate
# a otro jugador). Con esos datos se necesita saber:
# • Nombre del jugador más joven.
# • Jugador que más bajas tuvo.
# • Jugador con menos muertes
# • El promedio de bajas del equipo
# • La cantidad de jugadores que tienen entre 20 y 30 años cuyas bajas estan
# entre 10 y 20
# • El nombre y edad del jugador que más muertes tuvo (MVP)

# lista_jugadores = [{'nombre': 'juan', 'edad': 14, 'muertes': 2, 'bajas': 5}, {
#     'nombre': 'martin', 'edad': 43, 'muertes': 3, 'bajas': 7}]


# for i in range(2):

#     jugador = {}

#     while True:
#         try:
#             nombre = input('ingrese el nombre del jugador : ')
#             if (nombre != ''):
#                 break
#         except:
#             print('ingresa un valor valido')

#     jugador['nombre'] = nombre

#     while True:
#         try:
#             edad = int(input('ingresa la edad del jugador : '))
#             if (edad >= 8):
#                 break
#         except:
#             print('no es un valor valido')

#     jugador['edad'] = edad
#     while True:
#         try:
#             muertes = int(input('ingrese cuantas veces murio : '))
#             break
#         except:
#             print('no es un valor valido')

#     jugador['muertes'] = muertes

#     while True:
#         try:
#             bajas_condfirmadas = int(input('ingrese cuantas veces mato : '))
#             break
#         except:
#             print('no es un valor valido')

#     jugador['bajas'] = bajas_condfirmadas

#     lista_jugadores.append(jugador)

# print(lista_jugadores)


# for jugador in lista_jugadores:
#     print(lista_jugadores.index(jugador))
#     if (lista_jugadores.index(jugador) == 0 or jugador['edad'] < min_edad):

#         jugador_joven = jugador['nombre']
#         min_edad = jugador['edad']

# print(f'el jugador mas joven es {jugador_joven}')


# for jugador in lista_jugadores:
#     print(lista_jugadores.index(jugador))
#     if (lista_jugadores.index(jugador) == 0 or jugador['bajas'] > max_bajas):

#         jugador_mas_bajas = jugador['nombre']
#         max_bajas = jugador['bajas']

# print(f'el jugador con mas bajas fue es {jugador_mas_bajas}')


# 8-------------------------------------------

# Escribir un programa que le pida al usuario ingresar una lista de nombres de personas
# (previamente validada) y luego le pidan 1 solo nombre en específico. Se debe buscar
# el nombre especifico en la lista de nombres y si esta presente el programa deberá
# imprimir la posición del nombre en la lista, la posición de memoria donde se encuentra
# ese nombre y la cantidad de caracteres que tiene el nombre, si no se encuentra, se
# deberá informar por pantalla.

respuesta = 's'
lista_nombres = []

while respuesta == 's':
    while True:
        nombre = input('Ingrese un nombre para agregar a la lista: ')

        if (nombre != ''):
            break

    lista_nombres.append(nombre)

    respuesta = input('Desea ingresar otro nombre? (s/n): ')

while True:
    nombre_buscar = input('Ingrese el nombre a buscar: ')
    if (nombre_buscar != ""):
        break

for nombre in lista_nombres:
    if (nombre == nombre_buscar):
        print(
            f'el nombre esta en la lista en la posicion {lista_nombres.index(nombre)} , con el id {id(nombre_buscar)} y tiene {len(nombre_buscar)} caracteres')

if nombre_buscar in lista_nombres:
    print(
        f'el nombre esta en la lista en la posicion {lista_nombres.index(nombre_buscar)}, con el id {id(nombre_buscar)} y tiene {len(nombre_buscar)} caracteres')
else:
    print('el nombre no esta en la lista')


# 9---------------------------------------------

# Realizar un programa que pida una cadena de texto al usuario y le pida una cadena de
# texto y determine que la cadena ingresada es un palíndromo o no. De serlo deberá
# imprimir la palabra por consola.

# while True:
#     cadena = input('Ingrese un texto: ')
#     if(cadena != ""):
#         break

# if(list(cadena) == list(reversed(cadena))):
#     print('Es un palindromo')
# else:
#     print('No es un palindromo')


# 10------------------------------------------

# Se necesita un programa que solicite al usuario que ingrese una lista de números
# enteros de tamaño N. El programa deberá remover el valor máximo y mínimo de la
# lista y luego calcular y mostrar el promedio de los valores restantes y determinar si el
# promedio es mayor o menor que la diferencia entre el máximo y el mínimo valor
# previamente removido.

# respuesta = 's'
# lista_numeros = []
# acumulador = 0

# while respuesta == 's':
#     while True:
#         try:
#             numero = int(input('Ingrese un numero : '))
#             if (numero != ''):
#                 break

#         except:
#             print('El valor ingresado no es un numero')

#     lista_numeros.append(numero)

#     respuesta = input('Desea ingresar otro numero (s/n): ')

# diferencia = max(lista_numeros) - min(lista_numeros)

# lista_numeros.remove(max(lista_numeros))
# lista_numeros.remove(min(lista_numeros))

# if numero > 0 in lista_numeros:
#     acumulador += numero


# for numero in lista_numeros:
#     acumulador += numero

# promedio_numeros = acumulador / len(lista_numeros)

# print(lista_numeros)
# print(diferencia)
# print(promedio_numeros)

# if (promedio_numeros > diferencia):
#     print('El promedio de los numeros restantes es mayor que la diferencia de los valor maximos y minimos')
# else:
#     print('El promedio de los numeros restantes no es mayor que la diferencia de los valor maximos y minimos')
