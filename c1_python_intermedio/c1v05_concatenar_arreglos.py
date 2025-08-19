lista_append = [1, 2, 3]
lista_extend = [4, 5, 6]
lista_insert = [7, 8, 9]

lista_letras = ["a", "b", "c"]

# Append. se agrega la lista en la ultima posicion 
lista_append.append(lista_letras)
print(lista_append)

# Extend. se extiende la lista a la que le agregamos la funcion
lista_extend.extend(lista_letras)
print(lista_extend)

# Insert. el "1" indica la posicion donde queremos intrudcir la lista
lista_insert.insert(1, lista_letras)
print(lista_insert)
