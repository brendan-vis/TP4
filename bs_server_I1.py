import socket
import argparse
from sys import exit as sysexit


# On choisit une IP et un port où on va écouter
host = '10.1.1.11' # string vide signifie, dans ce conetxte, toutes les IPs de la machine

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', help="port utilisé",type=int, default=13337)
args = parser.parse_args()

port = args.port

if port < 0 or port > 65535:
    print(f"ERROR -p argument invalide. Le port spécifié {port} n'est pas un port valide (de 0 à 65535).")
    sysexit(1)
if port >= 0 and port <= 1024:
    print(f"ERROR -p argument invalide. Le port spécifié {port} est un port privilégié. Spécifiez un port au dessus de 1024.")
    sysexit(2)

parser.add_argument("-l", help="port utilisé",type=int)
if host != r'([0–9]{1,3}.){3}.([0–9]{1,3})':
    print(f"ERROR -l argument invalide. L'adresse {host} n'est pas une adresse IP valide.")
    sysexit(3)
# if host != :
#     print(f"")
args = parser.parse_args()
# print(args)


# On crée un objet socket
# SOCK_STREAM c'est pour créer un socket TCP (pas UDP donc)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# On demande à notre programme de se bind sur notre port
s.bind((host, port))  

# Place le programme en mode écoute derrière le port auquel il s'est bind
s.listen(1)
# On définit l'action à faire quand quelqu'un se connecte : on accepte
conn, addr = s.accept()
# Dès que quelqu'un se connecte, on affiche un message qui contient son adresse
print(f"Un client vient de se co et son IP c'est {addr}.")

# Petite boucle infinie (bah oui c'est un serveur)
# A chaque itération la boucle reçoit des données et les traite
while True:

    try:
        # On reçoit 1024 bytes de données
        data = conn.recv(1024)

        # Si on a rien reçu, on continue
        if not data: break

        if data == b"meo":
            conn.sendall(b"Meo a toi confrere.")
        elif data == b"waf":
            conn.sendall(b"ptdr t ki")
        else :
            conn.sendall(b"Mes respects humble humain.")

        # On affiche dans le terminal les données reçues du client
        print(f"Données reçues du client : {data}")

    except socket.error:
        print("Error Occured.")
        break

# On ferme proprement la connexion TCP
conn.close()
