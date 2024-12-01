import os
import trio
from samp_query import Client

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

async def main():
    try:
        # Dividir la entrada en IP y Puerto
        ip, port = server_address.split(':')
        port = int(port)

        # Crear un cliente SAMP
        client = Client(ip=ip, port=port)

        # Obtener información del servidor
        info = await client.info()
        print(GREEN + f"Servidor: {info.name}")
        print(CYAN + f"Jugadores: {info.players}/{info.max_players}")

        # Obtener lista de jugadores
        player_list = await client.players()
        print(RESET + "\nLista de jugadores conectados:")

        if player_list.players:
            for player in player_list.players:
                print(f"{CYAN}- {player.name} (Score: {player.score})")
        else:
            print(RED + "No hay jugadores conectados en este momento.")

        # Obtener reglas del servidor
        rule_list = await client.rules()
        print(RESET + "\nReglas del servidor:")
        for rule in rule_list.rules:
            print(f"{YELLOW}- {rule.name}: {rule.value}")

    except ValueError:
        print(RED + "Error: Ingresa la dirección en el formato correcto (IP:PUERTO).")
    except Exception as e:
        print(RED + f"Error: {str(e)}")

# Ejecutar el programa principal
trio.run(main)
