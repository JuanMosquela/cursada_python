from functions.funciones import pedir_texto


cadena = pedir_texto('Ingrese una cadena de texto: ')

# 1 ------------------------


def contar_caracteres(cadena):
    contador = 0
    for letra in cadena:
        contador += 1

    return contador


contador_caracteres = contar_caracteres(cadena)
print(f'La cantidad de caracteres de {cadena} es : {contador_caracteres}')

# 2 --------------------------


def eliminar_caracteres(cadena, caracter):

    nueva_cadena = cadena.replace(caracter, "")
    print(nueva_cadena)


caracter_eliminar = pedir_texto('Ingrese el caracter a eliminar : ')
eliminar_caracteres(cadena, caracter_eliminar)

# 3---- contar palabras


def contar_palabras(cadena):

    cantidad_palabras = len(cadena.split(" "))
    return cantidad_palabras


cantidad_palabras = contar_palabras(input('Ingrese una cadena : '))
print(f'La cantidad de palabras es de {cantidad_palabras}')


# 4-----  reemplazar palabras

def reemplazar_palabra(palabra_a_reemplazar, palabra_nueva, cadena):
    palabras_reemplazadas = cadena.replace(palabra_a_reemplazar, palabra_nueva)
    print(palabras_reemplazadas)


palabra_a_reemplazar = input(
    'Ingrese una palabra para reemplzar en la cadena: ')
palabra_nueva = input('Ingrese la palabra a insertar en su lugar: ')

reemplazar_palabra(palabra_a_reemplazar, palabra_nueva, cadena)


# 5---- encontrar patron

cadena = pedir_texto('Ingrese una cadena de texto: ')


def encontrar_patron(cadena, patron):

    lista_patron = list(patron)

    if patron in cadena:
        for letra in lista_patron:
            print(
                f'la letra {letra} se encontro en la posicion {cadena.index(letra)}')
    else:
        print('no se encontro un patron')


patron = pedir_texto('Ingrese un patron a buscar: ')
encontrar_patron(cadena, patron)
