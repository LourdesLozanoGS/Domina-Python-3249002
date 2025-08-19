from datetime import datetime

ahora = datetime.now()

# imprimir la fecha de ahora y el tipo de la avriable de ahora
print(ahora, type(ahora))

# de fecha a string
fecha = ahora.strftime("%Y-%m-%d")
print(fecha, type(fecha))

# formato 24h, solo H:M:S
format_24h = ahora.strftime("%H:%M:%S")
print(format_24h)

# formato 12h. "%P" es apra indicar si es AM o PM
format_12h = ahora.strftime("%I:%M:%S %p")
print(format_12h)

# def dates():

#     date = datetime.now()
#     new_format_24 = date.strftime('%H:%M:%S')
#     new_format_12 = date.strftime('%I:%M:%S %p')

#     print("date", date)
#     print("24 Hours: ", new_format_24)
#     print("AM/PM: ", new_format_12)
