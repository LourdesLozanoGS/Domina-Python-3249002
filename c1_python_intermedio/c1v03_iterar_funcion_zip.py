# ZIP: Sirve para evitar ciclos anidados. Retorna objeto iterable compuesto por tuplas con el menor numero de elementos

lista_nombres = ["Ana", "Paco", "Javier", "Emilio"]
lista_edades = [25, 27, 25, 26]

# Unimos las listas
datos_zip = zip(lista_nombres, lista_edades)

#Aqui se imprime que se crea un objeto de tipo zip en una posicion de memoria
print(datos_zip)

# para comvertir el objeto en una lista utilizamos la funcion "list"
print(list(datos_zip))

for nombre, edad in zip(lista_nombres, lista_edades):
    print(nombre, edad)

for nombre, edad in datos_zip:
    print(nombre, edad)

