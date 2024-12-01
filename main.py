import os
from samp_query import SAMPServer

# Colores
GREEN = '\033[32m'
CYAN = '\033[;36m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'

os.system("clear")

print(RED + """                                                           
 _____ _____ _____ _____    _____ _       _                      
|   __|  _  |     |  _  |  |   __| |_ ___| |_ _ _ ___    ___ _ _ 
|__   |     | | | |   __|  |__   |  _| .'|  _| | |_ -|  |_ -| | |
|_____|__|__|_|_|_|__|     |_____|_| |__,|_| |___|___|  |___|\_/ 
                                                                 """)
print(GREEN + "   » ᴛ. ꜱᴛᴀʀᴋ «")
print("")
print("╔ Ingresa la IP y Puerto de esta manera『 123.456.678:8080 』")

# Entrada del usuario
server_address = input("╚» ")
os.system("clear")

try:
    # Dividir la entrada en IP y Puerto
    ip, port = server_address.split(':')
    port = int(port)

    # Crear un cliente SAMP y realizar la consulta
    server = SAMPServer(ip, port)

    # Obtener información del servidor
    info = server.info()
    players = server.players()

    print(GREEN + f"Servidor: {info['hostname']}")
    print(YELLOW + f"Mapa: {info['mapname']}")
    print(CYAN + f"Jugadores: {info['players']} / {info['maxplayers']}")
    print(RESET + "\nLista de jugadores conectados:")

    if players:
        for player in players:
            print(f"{CYAN}- {player['name']} (Score: {player['score']})")
    else:
        print(RED + "No hay jugadores conectados en este momento.")

except ValueError:
    print(RED + "Error: Ingresa la dirección en el formato correcto (IP:PUERTO).")
except Exception as e:
    print(RED + f"Error: {str(e)}")
