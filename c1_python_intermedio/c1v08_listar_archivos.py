import os

def listar_archivos(ruta):

    lista_archivos = os.listdir(ruta) #listdir retorna la la lista con los elemento subicados en un directoiro
    return lista_archivos

ruta_absoluta = os.getcwd() # retorna la ruat del directorio donde corremos la ruta desde el temrinal
ruta_relativa = "c1_python_intermedio/" # la carpeta donde tenemos el archivo
archivos = listar_archivos(ruta_relativa)
print(archivos)
