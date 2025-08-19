try:
    print("Texto con formato {}".format())
except Exception as e:
    raise Exception("Ha ocurrido un error durante la ejecución")
# except Exception as e:
    # e.add_note("Ha ocurrido un error durante la ejecución")
    # print(e.__notes__) # se guardan las notas. aqui no se para el programa pero podemos ver lo que paso
