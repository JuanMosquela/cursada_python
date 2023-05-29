import functools

lista = [{"num": 2}, {"num": 3}, {"num": 5}]
numero = [2, 3, 5, 7]


# lista_filtrada = list(filter(lambda num: num == 3, lista))
# print(lista_filtrada)
acumulador = functools.reduce(lambda a, b: a + b["num"], lista, 0)
print(acumulador)
