import re


def email_valido(email):

    # se usa "r" para que no tome \ como escape
    # a-z: calquier caracter entre la "a" y la "z". 0-9: indica cualquier digito. 
    # el "+" indicia que peude haber mas d eun caracter de este tipo
    # el * busc auna o mas ocurrecnia dentro del nombre de usuario
    formato_valido = r"^([a-z0-9]+[.-_])*[a-z0-9]+@[a-z0-9-]+(\.[a-z]{2,})+$"
    # IGNORECASE hace que no distinga entre mayusculas y minusuclas
    if re.match(formato_valido, email, re.IGNORECASE):
        return True
    return False

valido = email_valido("lourLM@email.co")
print("Email valido:", valido)
