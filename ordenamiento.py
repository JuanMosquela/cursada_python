from functions.funciones import *
from data.data import *


lista = [8, 4, 2, 7, 5, 9]


# print(lista)
# normalized_data = normalize_data(lista_personajes)

# print(lista_personajes)

# print(normalized_data)

print(lista)


for i in range(0, len(lista) - 1):

    for j in range(i + 1, len(lista)):

        if lista[i] > lista[j]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux


print(lista)


# sorted_list = sort(lista_personajes, "nombre", "dsc")
# print(sorted_list)
