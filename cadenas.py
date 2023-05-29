# Cadenas

# se reserva una direccion de memoria para la cadena hola mundo y se lo relaciona con la variable x como valor

palabra = 'hola mundo'

# cada vez que se utilice palabra vamos a estar haciendo referecnai a esa direccion en memoria

palabra = "chau mundo"

# se crea una nueva direccion en memoria, y como se le asigna este nuevo valor a palabra se destruye la referencia anterior y ahora palabra pasa a tener una nueva direccion en memoria.

# Metodos de cadenas:

palabra.capitalize()  # vuelve mayus el primer caracter
palabra.upper()  # vuelve matus toda la cadena
palabra.lower()  # vuelve a minus toda la cadena
palabra.islower()  # devuelve true si es minuscula


# las cadenas pueden ser iterables

for letra in palabra:
    print(letra)

# no es posible asignarle un nuevo valor a alguna de las posiciones
# no puedo hacer palabra[0] = 'G', ya que es inmutable

# si quiesiera modificar alguna letra de esta cadena deberia primero volverla una lista

aux = list(palabra)

for i in range(len(aux)):
    if (aux[i].islower):
        aux[i] = aux[i].upper()

print(aux)

# el metodo join sirve para tomar una lista de caracteres y juntarlos en una cadena

x = "".join(aux)

print(x)

# el meotod split nos separa una cadena por un caracter que nosotros les pasemos, y nos devuelve una lista con esos valores
# si no le pasamos ningun valor lo separa por los espacios en blanco

print(palabra.split())

# metodo strip recibe un caracter como argumento y lo remueve de los extremos de la cadena

cadena_con_espacios = "00000hola mundo como estas00000"
nueva_cadena = cadena_con_espacios.strip("0")
print(nueva_cadena)  # nos devuelve hola mundo como estas

# el meotod FIND recibe un parametro y busca la primera ocurrencia de una cadena

# devuelve 0 porque encontro la h en la primera posicion
print(nueva_cadena.find('h'))

# el metodo COUNT nos indica cuandtas veces encuentra este patron dentro de la cadena

print(nueva_cadena.count('o'))  # devuelve 4 porque hay 4 os en la cadena

# el metodo REPLACE recibe dos parametros, uno a buscar y otro a actualizar

print(nueva_cadena.replace('mundo', 'chabon'))

# recodar que si queremos modificar la cadena original debemos pisar el valor


