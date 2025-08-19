# si no tenemos la libreria, pip install requets
import requests

request = requests.get('https://ident.me') # retorna ip publica del dispositivo que hace la peticion
ip_publica = request.text
print(ip_publica)

# instalamos pi install public-ip
import public_ip as ip

ip_publica_2 = ip.get()
print(ip_publica_2)
