import socket, sys
from re import compile as recompile
from sys import exit as sysexit

# On définit la destination de la connexion
host = '10.1.1.11'  # IP du serveur
port = 13337        # Port choisir par le serveur


motif1 = recompile(r"waf")
motif2 = recompile(r"meo")
# Création de l'objet socket de type TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    # Connexion au serveur
    s.connect((host, port))
    # note : la double parenthèse n'est pas une erreur : on envoie un tuple à la fonction connect()
    print(f"Connecté avec succès au serveur {host} sur le port {port}")
    user_input = input("Que veux-tu envoyer au serveur : ")

     # Envoi de data bidon
    if type(user_input) is str:
        if motif1.match(user_input) or motif2.match(user_input):
            print(f"yo")
            user_input = bytes(user_input, "utf-8")
            s.sendall(user_input)
        else:
            raise TypeError("Il manque le mot waf ou meo")
    else:
        raise TypeError("Seuls les strings sont autorisées")
   

    # On reçoit 1024 bytes qui contiennent peut-être une réponse du serveur
    data = s.recv(1024)

    # On libère le socket TCP
    s.close()

    # Affichage de la réponse reçue du serveur
    print(f"Le serveur a répondu {repr(data)}")
except:
    sysexit()